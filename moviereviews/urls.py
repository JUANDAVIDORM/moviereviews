from django.contrib import admin
from django.urls import path
from movie import views as movieViews  # <- Importa tus vistas desde la app "movie"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movieViews.home),           # <- Ruta principal
    path('about/', movieViews.about),    # <- Ruta de la página About
]
