from django.urls import path, include 
from . import views 

urlpatterns = [
    path('registration/', views.mould_registration, name="MouldRegistration"),
    path('<int:mould_id>/', views.mould_view, name = "MouldView"),
    path('update/', views.mould_update,name = "MouldUpdate"),
    path('mouldSearch/', views.mould_search, name = "MouldSearch"),
    path('data/<int:mould_id>/', views.mould_data_update, name = "MouldUpdate"),
    path('update/<int:mould_id>/', views.mould_value_update, name = "MouldValueUpdate"), 
    path('delete/<int:mould_id>/', views.mould_delete, name = "MouldDeleted"), 
    path('gclean/<int:mould_id>', views.general_cleaning, name = "Gcleaning"), 
    path('gclearnaccept/', views.general_cleaning_accept, name = "GcleanAccept"),
    path('inspect/', views.inspection_type_choice, name = "Inspect"), 
    path('inspect/mouldunload', views.mould_search, name = "MouldUnLoad"), 
    path('inspect/mouldInspect', views.mould_daily_inspection, name = "MouldInspect"), 
]