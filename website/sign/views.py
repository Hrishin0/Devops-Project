from django.http import HttpResponse
from django.shortcuts import render
from .models import Sign
# Create your views here.

def index(request):
    return render(request, 'sign/index.html')