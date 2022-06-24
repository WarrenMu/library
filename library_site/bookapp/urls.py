
from django.urls import URLPattern, re_path,path
from . import views
urlpatterns = [

    path('bookapp/', views.login_form, name="login"),
]
