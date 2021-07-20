from django.urls import path, include 
from . import views 

urlpatterns = [
    path('registration/', views.mould_registration, name="MouldRegistration"), 
]
