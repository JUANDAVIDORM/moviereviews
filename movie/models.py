from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True)
    genre = models.CharField(blank=True, max_length=250)  # <-- Nuevo campo
    year = models.IntegerField(blank=True, null=True)     # <-- Nuevo campo

    def __str__(self):
        return self.title

class News(models.Model):
    headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.headline
