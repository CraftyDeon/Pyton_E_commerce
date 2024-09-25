from django.shortcuts import render, redirect
# Create your views here.
from .models import Profile
from .form import UserRegisterForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
def index(request):
    return render(request, 'accounts/home.html')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user, profile_picture=form.cleaned_data['profile_picture'])
            profile.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def ulogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')
@login_required
def ulogout(request):
    logout(request)
    return redirect('/')
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {'form': form})
