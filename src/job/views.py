from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from .form import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter
# Create your views here.

def job_list(request):

    job_list       = Job.objects.all()
    jobsNumber     = job_list.count() 

    ## Filters ##

    myFilter = JobFilter(request.GET, queryset=job_list)
    job_list = myFilter.qs


    paginator = Paginator(job_list, 4) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

 
    context = {
        "jobs" : page_obj,
        "jobsNumber" : jobsNumber,
        "myFilter"   : myFilter,
    }

    return render(request, "job/job_list.html", context)



def job_detail(request, slug):

    job_detail = Job.objects.get(slug=slug)


    if request.method == "POST":
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform     = form.save(commit=False)
            myform.job = job_detail
            myform.save() 



    else:
        form = ApplyForm()

    context = {
        "jobs_details" : job_detail,
        "form"         : form
    }

    return render(request, "job/job_detail.html", context)


@login_required
def add_job(request):

    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.owner = request.user
            myForm.save()
            return redirect(reverse(job_list))
    else:
        form = JobForm()

    context = {
        "form": form
    }

    return render(request, "job/add_job.html", context)


