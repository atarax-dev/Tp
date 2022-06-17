from django.shortcuts import render

from tpapp.helpers import is_running


def index_view(request):
    """Retourne le rendu lié à la requête"""
    return render(request, 'index.html')


def explanations_view(request):
    """Retourne le rendu lié à la requête"""
    if request.method == "GET":
        return render(request, 'explanations.html')

    elif request.method == "POST":
        # On va chercher la donnée entrée par l'utilisateur
        site_to_test = request.POST.get("site-input")
        # On la rentre en paramètre de la fonction du test
        result = is_running(site_to_test)
        # On affiche un résultat en fonction de ce qui est retourné
        if result:
            result_message = "Ce site répond correctement"
            # On transmet ce message à la vue via le paramètre context
            return render(request, 'explanations.html', context={"result_message": result_message})
        else:
            result_message = "Ce site ne répond pas ou l'entrée est invalide"
            return render(request, 'explanations.html', context={"result_message": result_message})




