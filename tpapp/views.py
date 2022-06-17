from django.shortcuts import render


def index_view(request):
    """Retourne le rendu de la requête"""
    return render(request, 'index.html')


def explanations_view(request):
    """Retourne le rendu de la requête"""
    return render(request, 'explanations.html')
