from django.shortcuts import render

# Create your views here.

def home(request):
    template = "homeapp/home.html"
    return render(request, template)