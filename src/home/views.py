from django.shortcuts import render
from job.models import *
# Create your views here.

def home(request):
    job_list       = Job.objects.all()


    context = {
        "jobs" : job_list,

    }
    return render(request, 'home/index.html')
