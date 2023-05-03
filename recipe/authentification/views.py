from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login
# # Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Rediriger vers une page de confirmation ou de connexion
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signUp.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'signIn.html')
        else:
            error_message = 'Invalid username or password'
    else:
        error_message = ''
    return render(request, 'signIn.html', {'error_message': error_message})