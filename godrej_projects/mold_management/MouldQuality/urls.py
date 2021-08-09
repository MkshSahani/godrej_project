from django.urls import path
from . import views 

urlpatterns = [
    path('', views.QualityPageRender,name = "MouldQuality"), 
    path('ppm', views.ppmDataView, name = "ppmData"),
    path('mouldInspect', views.inspectionDataShow, name = "MouldInspectView"),  
    path('mouldSelect/', views.mold_name_select, name = "MouldNameSelect"), 
    path('historyCard/<int:mould_id>', views.mold_history_card), 

]
