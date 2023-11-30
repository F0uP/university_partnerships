from django.db import models
from universities.models import University

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    university_main = models.ForeignKey(University, on_delete=models.CASCADE, related_name="projects_universityMain")
    university_sec = models.ForeignKey(University, on_delete=models.CASCADE, related_name="projects_universitySec")

    def __str__(self):
        return f'{self.project_name} - {self.university_main} -> {self.university_sec}'