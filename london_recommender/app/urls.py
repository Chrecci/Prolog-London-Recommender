from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vibe/', views.get_vibe, name='vibe'),
    path('chill/', views.chill, name='chill'),
    path('result/', views.result, name='result'),
]
