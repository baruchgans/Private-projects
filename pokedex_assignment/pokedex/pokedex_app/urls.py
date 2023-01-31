from django.urls import path

from . import views

urlpatterns = [
    path('', views.pokedex, name='pokedex_default'),
    path('page/<int:page_number>/', views.pokedex, name='pokedex'),

]
