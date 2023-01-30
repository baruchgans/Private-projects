from django.urls import path

from . import views

urlpatterns = [
    path('page/<int:page_number>/', views.pokedex, name='pokedex'),

]
