from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper

from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets
import datetime
from .models import Activity, Vote
from crispy_forms.layout import Submit
from django.forms.widgets import RadioSelect

class ActivityForm(ModelForm):
	class Meta:
		model =  Activity
		exclude=['vote_score']

	def __init__(self, *args, **kwargs):
		super(ActivityForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class VoteForm(ModelForm):
	class Meta:
		DAY_CHOIE = [(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')]
		model =  Vote
		exclude=[]
		widgets = {
        'Day': RadioSelect(choices=DAY_CHOIE),
        }

	def __init__(self, *args, **kwargs):
		super(VoteForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit', onclick="window.history.back()"))
