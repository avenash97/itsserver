# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Farms, Household, Well
from django.core import serializers

def index(request):
	return HttpResponse('<h1 style="color:red;"> Welcome to Gis</h1>')

def farmsdetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'farms_detail': serializers.serialize('geojson', Farms.objects.all(),geometry_field='farm_polygon') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

def householddetail(request):
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'household_detail': serializers.serialize('geojson', Household.objects.all(),geometry_field='location') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res

def welldetail(request):
#	return HttpResponse('<h1 style="color:red;"> Welcome to Gis</h1>')
	if request.method == 'POST':
		username = request.POST.get('username', None)
		data = { 'well_detail': serializers.serialize('geojson', Well.objects.all(),geometry_field='location') }
		res = JsonResponse(data)
		res['Access-Control-Allow-Origin']="*"
		print(res)
		return res