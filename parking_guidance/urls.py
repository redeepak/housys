from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/floor1', views.floor1, name='floor1'),
]
