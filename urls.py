from django.urls import path 
from . import views

urlpatterns = [
    path('',views.indexview,name="home"),
    path('dashboard/',views.dashboard,name="dashboard"),
    # path('login/',),
    path('register/',views.registerview,name="register_urls"),
    # path('logout/',),    
]