from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializer import UniversitySerializer
from .models import University
from rest_framework import status

# Create your views here.
#index view
def index(request):
    return render(request, 'index.html')

class UniversityApiView(ViewSet):
    def get(self, request, *args, **kwargs):
        return Response(UniversitySerializer(University.objects.all(), many = True).data, status=status.HTTP_200_OK)
    
    def getById(self, request, *args, **kwargs):
        searched_id = request.data.get('id')
        university = University.objects.filter(id=searched_id)
        if not university:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UniversitySerializer(university)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def getByName(self, request, *args, **kwargs):
        searched_id = request.data.get('name')
        university = University.objects.filter(name=searched_id)
        if not university:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UniversitySerializer(university)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'name' : request.data.get('name'),
            'url' : request.data.get('url'),
            'address' : request.data.get('address'),
            'partner' : request.data.get('partner'),
        }
        serializer = UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

