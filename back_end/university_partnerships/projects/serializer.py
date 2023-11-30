from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ["name", "description", "url", "uni1", "uni2"]

    def create(self, validated_data):
        university1 = validated_data.pop('uni1')
        university2 = validated_data.pop('uni2')
        new_project = Project.objects.create(**validated_data)
        new_project.university_main = university1
        new_project.university_sec = university2
        new_project.save()
        return new_project