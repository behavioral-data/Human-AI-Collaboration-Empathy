from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.
def index(request):
	# Load a seeker post (e.g., from a datahase)
	seeker_post = "My job is becoming more and more stressful with each passing day."

	return render(request, "feedback_interface/index.html", {'treated': 1, 'SP': seeker_post})
