from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializer import ProjectSerializer
from .models import Project
from rest_framework import status
from rest_framework.request import Request

# Create your views here.
#index view
def index(request):
    return render(request, 'index.html')

class ProjectApiView(ViewSet):
    def get(self, request, *args, **kwargs):
        return Response(ProjectSerializer(Project.objects.all(), many = True).data, status=status.HTTP_200_OK)
    
    def getById(self, request : Request, *args, **kwargs):
        searched_id = request.data.get('id')
        project = Project.objects.filter(id=searched_id)
        if not project:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def getByName(self, request, *args, **kwargs):
        searched_id = request.data.get('name')
        project = Project.objects.filter(name=searched_id)
        if not project:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name' : request.data.get('name'),
            'description' : request.data.get('description'),
            'url' : request.data.get('url'),
            'address' : request.data.get('address'),
            'universityMain' : request.data.get('universityMain'),
            'universitySec' : request.data.get('universitySec'),
        }
        serializer = ProjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

