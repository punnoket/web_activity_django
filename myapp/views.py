from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .forms import ActivityForm
from models import Activity
# Create your views here.
def home(request):
	return render(request, 'home.html', {'key': "value" })

def hike(request):
	return render(request, 'hike.html', {'key': "value" })

def vote(request):
	score = request.GET.get("days")
	print(score)
	##return redirect('home')
	return render(request, 'home.html', {'key': "value" })

class CreateActivity(CreateView):
	queryset = Activity()
	template_name='add.html'
	form_class = ActivityForm
	success_url = '/'