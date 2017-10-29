from django.contrib import admin

from django.contrib.gis import admin
from .models import Farms, Household, Well

admin.site.register(Farms, admin.OSMGeoAdmin)
admin.site.register(Household, admin.OSMGeoAdmin)
admin.site.register(Well, admin.OSMGeoAdmin)