from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('save-data/', views.save_data, name='save_data'),
    path('view-data/', views.view_data, name='view_data'),
]

