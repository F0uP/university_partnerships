from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UniversitySerializer

# Create your views here.
#index view
def index(request):
    return render(request, 'index.html')

#adding an university
@api_view(['POST'])
def add_univeristy(request, format=None):
    serializer = UniversitySerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['response'] = "Data sucessfully safed"
        return Response(data)
    return Response(serializer.errors)

