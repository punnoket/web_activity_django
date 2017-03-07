from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html', {'key': "value" })

def hike(request):
	return render(request, 'hike.html', {'key': "value" })

def vote(request):
	score = request.POST.get("day")
	print(score)
	return render(request, 'home.html', {'key': "value" })
