from django.shortcuts import render
from .models import Movie  # Importamos el modelo Movie

def home(request):
    # Obtener lo que el usuario escribió en el buscador (puede ser None)
    searchTerm = request.GET.get('searchMovie')

    if searchTerm:
        # Si escribió algo, buscar películas cuyo título contenga ese texto
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        # Si no escribió nada, mostrar todas las películas
        movies = Movie.objects.all()

    # Enviamos la lista de películas y tu nombre a la plantilla
    return render(request, 'home.html', {
        'name': 'David Ortiz Moncada',
        'movies': movies
    })

def about(request):
    return render(request, 'about.html')
