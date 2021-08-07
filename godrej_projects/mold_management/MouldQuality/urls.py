from django.urls import path
from . import views 

urlpatterns = [
    path('', views.QualityPageRender,name = "MouldQuality"), 
    path('ppm', views.ppmDataView, name = "ppmData"), 
]
