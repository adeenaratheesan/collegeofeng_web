from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'home_templates/homepage.html')


# def homepage(request):
#     return render(request,'home_templates/homepage.html')
