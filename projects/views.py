from django.shortcuts import render
from django.http import HttpResponse
from projects.models import Project

# Create your views here.
def project_list(request):
    # Return httpresponse object
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, 'projects/index.html')

def all_projects(request):
    # query the db to return all project objects
    # {{variable}}
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html',
                  {'projects': projects})
