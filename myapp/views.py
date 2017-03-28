from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import ActivityForm
from models import Activity
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from models import Activity, Vote
from myapp.forms import ActivityForm, VoteForm
from django.contrib.auth.decorators import login_required

username = ""

# Create your views here.
def home(request):

    username = str(request.session.get('user'))
    return render(request, 'home.html', {'key': "value" })


def all_activity(request):
	id = 1;

	activities = Activity.objects.all()
	return render(request, 'AllAc.html',{'activity': activities})

def vote(request, id=1):
	activity = Activity.objects.get(id=id);
	##return redirect('home')

	return render(request, 'vote.html', {'activity': activity ,'id':id})

def voteScore(request, id=1):
	score = request.GET.get("day")
	activity = Activity.objects.get(id=id);
	vote = Vote.objects.create(days=score)
	vote.user = request.session.get('user')
	vote.activity = activity
	vote.save()
	print(score)
	return redirect('home')

def showVoteScore(request, id=1):
	monday = 0;tuesday = 0; wednesday = 0; thursday = 0; friday = 0
	activity = Activity.objects.get(id=id);
	scoreResult = Vote.objects.filter(activity_id = id)
	dayStr=""


	for i in scoreResult:
		dayStr = str(i.days)+"s"
		if(dayStr == "Mondays"):
			monday+=1
		if(dayStr == "Tuesdays"):
			tuesday+=1
		if(dayStr == "Wednesdays"):
			wednesday+=1
		if(dayStr == "Thursdays"):
			thursday+=1
		if(dayStr == "Fridays"):
			friday+=1


	dayResult = [monday,tuesday,wednesday,thursday,friday]
	dayList = ["monday", "tuesday", "wednesday", "thursday", "friday"]
	dayDic =  {"monday":monday, "tuesday":tuesday, "wednesday": wednesday, "thursday": thursday, "friday": friday}
	print(dayDic["monday"])
	return render(request, 'show_score_vote.html', {'activity': activity, "dayList": dayList, "dayResult":dayResult})

class CreateActivity(CreateView):
	queryset = Activity()
	template_name='activity.html'
	form_class = ActivityForm
	success_url = '/'

class CreateVoteActivity(CreateView):
	queryset = Vote()
	template_name='vote_test.html'
	form_class = VoteForm
	success_url = '/'
