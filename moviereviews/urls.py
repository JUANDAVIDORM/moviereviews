from django.contrib import admin
from django.urls import path, include
from movie import views as movie_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name='home'),
    path('about/', movie_views.about, name='about'),
    path('news/', include('news.urls')),
    path('login/', movie_views.login_view, name='login'),
    path('signup/', movie_views.signup, name='signup'),
    path('statistics/', movie_views.statistics_view, name='statistics'),
    path('genre-statistics/', movie_views.genre_statistics_view, name='genre_statistics'),
    path('statistics-both/', movie_views.statistics_both_view, name='statistics_both'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
