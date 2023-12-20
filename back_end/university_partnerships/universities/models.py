from django.db import models
import requests
from site_info.models import Site_info

# Create your models here.
class University(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    address = models.CharField(max_length=200)
    # dont get inserted manually, but can
    lat = models.CharField(max_length=10, blank=True)
    lng = models.CharField(max_length=10, blank=True)
    partner_universities = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        def getCoordinates(address):
            google_key = Site_info.get_solo().google_api_key
            resp = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=" + google_key, timeout=3000)
            if resp.status_code == 200:
                data = resp.json()
                try:
                    return data["results"][0]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lng"]
                except:
                    # try with places api
                    try:
                        data = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + address + "&key=" + google_key, timeout=3000).json()
                        return data["results"][0]["geometry"]["location"]["lat"], data["results"][0]["geometry"]["location"]["lng"]
                    except:
                        print("ERROR: Had problems finding coordinates for address " + address + " response was:\n", data)
                        return 0,0
            else:
                print("Error: Check your Google Maps API Key")
                return 0,0
        self.lat, self.lng = getCoordinates(self.address.strip(" ").replace(" ", "%20"))
        super(University, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Universitie"