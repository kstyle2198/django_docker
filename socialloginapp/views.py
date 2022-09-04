from django.shortcuts import render

# Create your views here.

def socialloginmain(request):
    return render(request, 'index1.html')

def sociallogin(request):
    return render(request, 'login1.html')

