from django.db import models
from solo.models import SingletonModel

# Create your models here.
class Site_info(SingletonModel):
    google_api_key = models.CharField(max_length=1000)
    site_name = models.CharField(max_length=250, default="University_Partnerships")

    def __str__(self):
        return "global site setting setup"
    
    def __unicode__(self):
        return u"Site Information"

    class Meta:
        verbose_name = "site_info"
    