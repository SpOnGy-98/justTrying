from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello Buddy!")

def home(request):
    return render(request, 'html/home.html')

def register(request):
    return render(request, 'html/register.html')