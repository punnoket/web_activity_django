from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from models import Activity
from myapp.forms import ActivityForm

# Create your views here.
def home(request):
	return render(request, 'home.html', {'key': "value" })

def hike(request):
	return render(request, 'hike.html', {'key': "value" })

def all_activity(request):
	id = 1;
	activities = Activity.objects.all()
	return render(request, 'AllAc.html',{'activity': activities})

def vote(request, id=1):
	score = request.GET.get("day")
	print(score)
	activity = Activity.objects.get(id=id);
	##return redirect('home')
	return render(request, 'vote.html', {'activity': activity })

def voteScore(request, id=1):
	score = request.GET.get("day")
	print(score)
	return redirect('home')

class CreateActivity(CreateView):
	queryset = Activity()
	template_name='activity.html'
	form_class = ActivityForm
	success_url = '/'
