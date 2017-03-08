from django.shortcuts import render

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
