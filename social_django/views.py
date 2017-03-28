from django.conf import settings
from django.contrib.auth import login, REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache
from django.shortcuts import render, redirect
from social_core.utils import setting_name
from social_core.actions import do_auth, do_complete, do_disconnect
from .utils import psa
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.core import serializers

NAMESPACE = getattr(settings, setting_name('URL_NAMESPACE'), None) or 'social'


def login_facebook(request):
    context = {}
    template = 'test_auth.html'
    return render(request, template, context)

def members(request):
    context = {}
    template = 'members.html'
    return render(request, template, context)

def logout(request):
    auth_logout(request)
    return redirect('/')

def social_user(backend, uid, user=None, *args, **kwargs):
    '''OVERRIDED: It will logout the current user
    instead of raise an exception '''

    provider = backend.name
    social = backend.strategy.storage.user.get_social_auth(provider, uid)
    if social:
        if user and social.user != user:
            logout(backend.strategy.request)
            #msg = 'This {0} account is already in use.'.format(provider)
            #raise AuthAlreadyAssociated(backend, msg)
        elif not user:
            user = social.user
    return {'social': social,
            'user': user,
            'is_new': user is None,
            'new_association': False}

@never_cache
@psa('{0}:complete'.format(NAMESPACE))
def auth(request, backend):

    return do_auth(request.backend, redirect_name=REDIRECT_FIELD_NAME)


@never_cache
@csrf_exempt
@psa('{0}:complete'.format(NAMESPACE))
def complete(request, backend, *args, **kwargs):
    """Authentication complete view"""
    print(request.user)
    request.session['username'] = request.user.username

    return do_complete(request.backend, _do_login, request.user,
                       redirect_name=REDIRECT_FIELD_NAME, *args, **kwargs)


@never_cache
@login_required
@psa()
@require_POST
@csrf_protect
def disconnect(request, backend, association_id=None):
    """Disconnects given backend from current logged in user."""
    return do_disconnect(request.backend, request.user, association_id,
                         redirect_name=REDIRECT_FIELD_NAME)


def _do_login(backend, user, social_user):
    user.backend = '{0}.{1}'.format(backend.__module__,
                                  backend.__class__.__name__)
    auth_login(backend.strategy.request, user)
    if backend.setting('SESSION_EXPIRATION', False):
        # Set session expiration date if present and enabled
        # by setting. Use last social-auth instance for current
        # provider, users can associate several accounts with
        # a same provider.
        expiration = social_user.expiration_datetime()
        if expiration:
            try:
                backend.strategy.request.session.set_expiry(
                    expiration.seconds + expiration.days * 86400
                )
            except OverflowError:
                # Handle django time zone overflow
                backend.strategy.request.session.set_expiry(None)
