from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .csv_tool import  read_data



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

    project_list = read_data()
    return Response(project_list)


def project(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'components/project.html')

@api_view(['POST'])
def post_issue(request, pk):
    print(request.POST)
    return Response({'result' : 'ok'})
