from django.urls import path, include 
from . import views 

urlpatterns = [
    path('registration/', views.mould_registration, name="MouldRegistration"), 
    path('<int:mould_id>/', views.mould_view, name = "MouldView")
]
