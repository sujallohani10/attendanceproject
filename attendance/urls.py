from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='attendance'),
    path('startshift', views.startShift, name='startshift'),
    path('endshift', views.endShift, name='endshift'),
]