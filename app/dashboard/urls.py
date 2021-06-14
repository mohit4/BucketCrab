from django.urls import path

app_name = 'dashboard'

from .views import DashboardView

urlpatterns = [
    
    path( 'dashboard/', DashboardView.as_view(), name='dashboard' ),

]
