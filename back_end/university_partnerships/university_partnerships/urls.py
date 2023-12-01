"""university_partnerships URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from universities.views import UniversityApiView
from projects.views import ProjectApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('universities.urls')),
    path('api/allProject', ProjectApiView.as_view({"get" : "get"})),
    path('api/getProjectById', ProjectApiView.as_view({"get" : "getById"})),
    path('api/getProjectByName', ProjectApiView.as_view({"get" : "getByName"})),
    path('api/allUniversity', UniversityApiView.as_view({"get" : "get"})),
    path('api/getUniversityById', UniversityApiView.as_view({"get" : "getById"})),
    path('api/getUniversityByName', UniversityApiView.as_view({"get" : "getByName"})),
]
