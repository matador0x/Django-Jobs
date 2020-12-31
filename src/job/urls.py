from django.urls import path
from . import views
from . import api

app_name = 'jobs'
urlpatterns = [
    
    path('', views.job_list, name="job_list"),
    path('add', views.add_job, name="add_job"),
    path('<str:slug>', views.job_detail, name="job_detail"),

    ## API PATHS
    path('api/jobs', api.job_List_API, name="job_List_API"),
    path('api/jobs/<int:id>', api.job_details_api, name="job_details_api"),

]
