from django.contrib import admin
from site_info.models import Site_info
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(Site_info, SingletonModelAdmin)