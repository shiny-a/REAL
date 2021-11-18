from django.shortcuts import render

# Create your views here.

def Top(request):
    return render(request, 'base.html')