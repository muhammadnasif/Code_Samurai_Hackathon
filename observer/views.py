from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .csv_tool import  read_data


def load(request):
    return render(request, 'base/base.html')

@api_view(['GET'])
def projects(request):
    project_list = read_data()
    return Response(project_list)

@api_view(['POST'])
def post_issue(request, pk):
    print(request.POST)
    return Response({'result' : 'ok'})
