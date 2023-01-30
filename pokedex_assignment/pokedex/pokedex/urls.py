from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('pokedex_app/', include('pokedex_app.urls')),
    path('admin/', admin.site.urls),
]