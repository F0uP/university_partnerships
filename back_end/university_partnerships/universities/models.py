from django.db import models

# Create your models here.
class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    partner_universities = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name