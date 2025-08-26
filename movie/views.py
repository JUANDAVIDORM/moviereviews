from django.shortcuts import render
from .models import Movie
from news.models import News

def home(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    news = News.objects.order_by('-date')[:5]  # Últimas 5 noticias
    return render(request, 'home.html', {'movies': movies, 'news': news})

def about(request):
    return render(request, 'about.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email': email})

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import urllib, base64
from .models import Movie
from django.shortcuts import render

def statistics_view(request):
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        count = movies_in_year.count()
        movie_counts_by_year[year] = count

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))

    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.subplots_adjust(bottom=0.3)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    plt.close()

    return render(request, 'statistics.html', {'graphic': graphic})

def genre_statistics_view(request):
    # Obtener todas las películas
    movies = Movie.objects.all()
    genre_counts = {}

    for movie in movies:
        # Considera solo el primer género (si hay varios separados por coma)
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
        else:
            first_genre = "None"
        genre_counts[first_genre] = genre_counts.get(first_genre, 0) + 1

    # Crear la gráfica
    bar_width = 0.5
    bar_positions = range(len(genre_counts))
    plt.figure(figsize=(10,5))
    plt.bar(bar_positions, genre_counts.values(), width=bar_width, align='center')
    plt.title('Movies per genre')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, genre_counts.keys(), rotation=45, ha='right')
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    plt.close()

    return render(request, 'genre_statistics.html', {'graphic': graphic})

def statistics_both_view(request):
    # --- Gráfica por año ---
    years = Movie.objects.values_list('year', flat=True).distinct().order_by('year')
    movie_counts_by_year = {}
    for year in years:
        if year:
            movies_in_year = Movie.objects.filter(year=year)
        else:
            movies_in_year = Movie.objects.filter(year__isnull=True)
            year = "None"
        count = movies_in_year.count()
        movie_counts_by_year[year] = count

    bar_width = 0.5
    bar_positions = range(len(movie_counts_by_year))
    plt.figure(figsize=(8,4))
    plt.bar(bar_positions, movie_counts_by_year.values(), width=bar_width, align='center', color='blue')
    plt.title('Movies per year')
    plt.xlabel('Year')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, movie_counts_by_year.keys(), rotation=90)
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic_year = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    # --- Gráfica por género ---
    movies = Movie.objects.all()
    genre_counts = {}
    for movie in movies:
        if movie.genre:
            first_genre = movie.genre.split(',')[0].strip()
        else:
            first_genre = "None"
        genre_counts[first_genre] = genre_counts.get(first_genre, 0) + 1

    bar_width = 0.5
    bar_positions = range(len(genre_counts))
    plt.figure(figsize=(8,4))
    plt.bar(bar_positions, genre_counts.values(), width=bar_width, align='center', color='green')
    plt.title('Movies per genre (first only)')
    plt.xlabel('Genre')
    plt.ylabel('Number of movies')
    plt.xticks(bar_positions, genre_counts.keys(), rotation=45, ha='right')
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graphic_genre = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    plt.close()

    return render(request, 'statistics_both.html', {
        'graphic_year': graphic_year,
        'graphic_genre': graphic_genre
    })