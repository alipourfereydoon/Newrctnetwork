from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home),
    path('contact_us',views.contact_us),
]