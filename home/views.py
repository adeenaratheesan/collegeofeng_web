from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'home_templates/homepage.html')


def homepage(request):
    return render(request,'home_templates/homepage.html')

def login(request):
    return render(request,'home_templates/login.html')

def onlineadmission(request):
    return render(request,'home_templates/onlineadmission.html')

def sample(request):
    return render(request,'home_templates/sample.html')
