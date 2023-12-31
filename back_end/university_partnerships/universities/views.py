from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializer import UniversitySerializer
from .models import University
from rest_framework import status
from site_info.models import Site_info

# Create your views here.
#index view
def index(request):
    return render(request, 'index.html', {"google_api_key" : Site_info.get_solo().google_api_key, 
                                          "universities" : University.objects.all(), 
                                          "site_url" : Site_info.get_solo().site_url,
                                          "site_name" : Site_info.get_solo().site_name})

class UniversityApiView(ViewSet):
    def get(self, request, *args, **kwargs):
        return Response(UniversitySerializer(University.objects.all(), many = True).data, status=status.HTTP_200_OK)
    
    def getById(self, request, *args, **kwargs):
        searched_id = request.data.get('id')
        university = University.objects.filter(id=searched_id)
        if not university:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UniversitySerializer(university.get())
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def getByName(self, request, *args, **kwargs):
        searched_id = request.data.get('name')
        university = University.objects.filter(name=searched_id)
        if not university:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UniversitySerializer(university.get())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'name' : request.data.get('name'),
            'url' : request.data.get('url'),
            'address' : request.data.get('address'),
            'partner_universities' : request.data.get('partner_universities'),
        }
        serializer = UniversitySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

