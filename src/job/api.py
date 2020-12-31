from .models import Job
from .serializers import jobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def job_List_API(request):
    all_jobs = Job.objects.all()
    data = jobSerializers(all_jobs, many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_details_api(request, id):
    job_detail = Job.objects.get(id=id)
    data = jobSerializers(job_detail).data
    return Response({'data':data})