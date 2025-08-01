from django.shortcuts import render

def home(request):
    context = {'name': 'David Ortiz Moncada'}  # Diccionario con el parámetro
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
