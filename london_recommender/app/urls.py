from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.get_name, name='name'),
    path('result/', views.result, name='result'),
]
