from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    '''
        Cette fonction est la page d'accueil du site
    '''
    return render(request, 'blog/home.html')
