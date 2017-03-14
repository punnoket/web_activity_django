"""ProjectAct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from myapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^auth/',include('wl_auth.urls',namespace="wl_auth")),
    url(r'^home/', views.home,name="home"),
    url(r'^$', views.home, name='home'),
    url(r'^vote/(?P<id>[0-9]+)$', views.vote,name = "vote"),
    url(r'^vote_score/(?P<id>[0-9]+)$', views.voteScore,name = "vote_score"),
    url(r'^all_activity/', views.all_activity,name = "all_activity"),
    url(r'^add_activity/$', views.CreateActivity.as_view(),name = "add_activity"),
    url(r'^vote_test/$', views.CreateVoteActivity.as_view(),name = "vote_test"),
    url(r'^show_score_vote/(?P<id>[0-9]+)$', views.showVoteScore,name = "show_score_vote"),


    # url(r'^$',Redirectview.as_view(url="/main/home/"),name='index'),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# if settings.DEBUG:
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
