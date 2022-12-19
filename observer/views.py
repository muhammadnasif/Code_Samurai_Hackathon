from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .csv_tool import  read_data
from .models import *
# Create your views here.


def load(request):
    return render(request, 'base/base.html')

@api_view(['GET'])
def projects(request):
    read_data()
    project_list = Project.objects.all()
    project_list = [
        {
            'project_name': p.name,
            'category': p.category,
            'affliated_agency' : [
                [{
                    'name': a.name,
                    'id': a.id,
                } for a in p.affiliated_agencies.all()]
            ],
            'description': p.description,
            'project_start_time': p.start_time,
            'project_completion_time': p.completion_time,
            'total_budget': p.total_budget,
            'completion_percentage': p.completion_percentage,
            'location_coordinates': [{
                'coord': [loc.longitude, loc.latitude],
                'id': loc.id,
            } for loc in p.location_set.all()],
            'id': p.id,
        } for p in Project.objects.all()
    ]
    return Response(project_list)


def project(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'components/project.html')

@api_view(['POST'])
def post_issue(request, pk):
    print(request.POST)
    return Response({'result' : 'ok'})
