from django.db import models
from universities.models import University

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=200)
    universityMain = models.ForeignKey(University, on_delete=models.CASCADE, related_name="projects_universityMain")
    universitySec = models.ForeignKey(University, on_delete=models.CASCADE, related_name="projects_universitySec")

    def __str__(self):
        return f'{self.name} - {self.universityMain} -> {self.universitySec}'