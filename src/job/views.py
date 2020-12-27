from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator

# Create your views here.

def job_list(request):

    job_list       = Job.objects.all()
    jobsNumber     = job_list.count() 
    
    paginator = Paginator(job_list, 4) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    context = {
        "jobs" : page_obj,
        "jobsNumber" : jobsNumber,
    }

    return render(request, "job/job_list.html", context)



def job_detail(request, slug):

    job_detail = Job.objects.get(slug=slug)

    context = {
        "jobs_details" : job_detail
    }

    return render(request, "job/job_detail.html", context)
