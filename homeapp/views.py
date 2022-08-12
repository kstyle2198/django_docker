from django.shortcuts import render
from .models import Portfolio, About

# Create your views here.

def home(request):
    template = "homeapp/home.html"
    
    data1 = Portfolio.objects.all()
    data2 =  About.objects.all()
    context = {'portfolios': data1, 'abouts': data2}
    return render(request, template, context)