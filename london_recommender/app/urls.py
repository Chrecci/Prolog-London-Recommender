from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vibe/', views.get_vibe, name='vibe'),
    path('chill/', views.chill, name='chill'),
    path('work/', views.work, name='work'),
    path('walk/', views.walk, name='walk'),
    path('active/', views.active, name='active'),
    path('goodfood/', views.goodfood, name='goodfood'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('price/', views.price, name='price'),
    path('energetic/', views.energetic, name='energetic'),
    path('result/', views.result, name='result'),
]
