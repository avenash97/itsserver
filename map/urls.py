from django.conf.urls import include, url
from . import views

urlpatterns = [
    url( r'^$' , views.index , name='index' ),
    url( r'^farmsdetail/' , views.farmsdetail , name='farmsdetail' ),
    url( r'^householddetail/' , views.householddetail , name='householddetail' ),
    url( r'^welldetail/' , views.welldetail , name='welldetail' ),    
]
