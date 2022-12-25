from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from . import forms

def login_page(request):
    '''
        Cette fonction permet de vérifier les paramètres de connexion d'un user
        Si les paramètres sont correctes, l'utilisateur est authentifier via
        authenticate ensuite l'utilisateur est loger. 
    '''
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                message = "Problème d'identification"
    return render(request, 'authentication/login.html', context={'form':form, 'message':message})

def logout_user(request):
    '''
    Cette fonction permet de déconnecter un utilisateur (user)
    '''
    logout(request)
    return redirect('login')
