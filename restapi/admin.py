from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Farm,admin.OSMGeoAdmin)
admin.site.register(Crop,admin.OSMGeoAdmin)
admin.site.register(Household,admin.OSMGeoAdmin)
admin.site.register(Season,admin.OSMGeoAdmin)
admin.site.register(Well,admin.OSMGeoAdmin)
admin.site.register(Member,admin.OSMGeoAdmin)
admin.site.register(Storage,admin.OSMGeoAdmin)
admin.site.register(storage_photo,admin.OSMGeoAdmin)
admin.site.register(farm_photo,admin.OSMGeoAdmin)
admin.site.register(well_photo,admin.OSMGeoAdmin)
admin.site.register(household_photo,admin.OSMGeoAdmin)
admin.site.register(storage_video,admin.OSMGeoAdmin)
admin.site.register(farm_video,admin.OSMGeoAdmin)
admin.site.register(well_video,admin.OSMGeoAdmin)
admin.site.register(household_video,admin.OSMGeoAdmin)
admin.site.register(household_audio,admin.OSMGeoAdmin)
