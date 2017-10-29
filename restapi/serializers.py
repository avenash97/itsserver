from rest_framework import serializers
from restapi.models import *
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        geo_field = "Location"
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        geo_field = "Location"
        fields = '__all__'

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        geo_field = "Location"
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class YieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yield
        fields = '__all__'

class farmphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = farm_photo
        geo_field = "Location"
        fields = '__all__'

class storagephotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = storage_photo
        geo_field = "Location"
        fields = '__all__'

class wellphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = well_photo
        geo_field = "Location"
        fields = '__all__'

class farmvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = farm_video
        geo_field = "Location"
        fields = '__all__'

class storagevideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = storage_video
        geo_field = "Location"
        fields = '__all__'

class wellvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = well_video
        geo_field = "Location"
        fields = '__all__'

class householdvideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = household_video
        geo_field = "Location"
        fields = '__all__'

class householdaudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = household_audio
        geo_field = "Location"
        fields = '__all__'

class householdphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = household_photo
        geo_field = "Location"
        fields = '__all__'

