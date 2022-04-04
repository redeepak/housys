from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/floor1', views.floor1, name='floor1'),
    path('/floor2', views.floor2, name='floor2'),
    path('/floor3', views.floor3, name='floor3'),
]
