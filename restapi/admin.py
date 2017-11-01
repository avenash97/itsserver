from django.contrib.gis import admin
from .models import *

# Register your models here.

admin.site.register(Farm,admin.GeoModelAdmin)
admin.site.register(Crop,admin.GeoModelAdmin)
admin.site.register(Household,admin.GeoModelAdmin)
admin.site.register(Season,admin.GeoModelAdmin)
admin.site.register(Well,admin.GeoModelAdmin)
admin.site.register(Member,admin.GeoModelAdmin)
admin.site.register(Storage,admin.GeoModelAdmin)
admin.site.register(storage_photo,admin.GeoModelAdmin)
admin.site.register(farm_photo,admin.GeoModelAdmin)
admin.site.register(well_photo,admin.GeoModelAdmin)
admin.site.register(household_photo,admin.GeoModelAdmin)
admin.site.register(storage_video,admin.GeoModelAdmin)
admin.site.register(farm_video,admin.GeoModelAdmin)
admin.site.register(well_video,admin.GeoModelAdmin)
admin.site.register(household_video,admin.GeoModelAdmin)
admin.site.register(household_audio,admin.GeoModelAdmin)
