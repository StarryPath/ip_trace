from django.urls import path

from . import views

urlpatterns = [
    path('raw', views.raw, name='raw'),
    path('logic', views.logic, name='logic'),
    path('alias',views.alias,name='alias'),
    path('tree',views.tree,name='tree'),
    path('nm',views.nm,name='nm'),
    path('',views.index,name='index'),
    path('trace', views.trace, name='trace'),
    path('pie', views.pie, name='pie'),
]