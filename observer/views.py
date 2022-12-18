from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import csv

from django.conf import settings



# Create your views here.

def load(request):
    return render(request, 'base/base.html')


@api_view(['GET'])
def projects(request):
    
    projects = []
    
    with open(settings.BASE_DIR / 'projects.csv', 'r') as file:
        reader = csv.reader(file)
        first = True
        for row in reader:
            if first:
                attributes = row
                first = False
            else:
                data = {}
                for i in range(len(attributes)):
                    data[attributes[i]] = row[i]
            
                projects.append(data)

    return Response(projects)

