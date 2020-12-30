from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contactForm(request):
    return HttpResponse("Contact")