from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProjectSerializer

# Create your views here.
#adding an university
@api_view(['POST'])
def add_project(request, format=None):
    serializer = ProjectSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['response'] = "Data sucessfully safed"
        return Response(data)
    return Response(serializer.errors)


