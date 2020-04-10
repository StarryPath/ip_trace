from django.urls import path

from . import views

urlpatterns = [
    path('raw', views.raw, name='raw'),
    path('logic', views.logic, name='logic'),
]