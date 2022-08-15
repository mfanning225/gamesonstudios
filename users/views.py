from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Country, City, StateProvince, UserProfile
from .forms import CustomuserCreationForm, UserProfileForm
from snake.models import SnakeHighScore
from leaderboard.filters import SnakeHighScoreFilter


def loginUser(request):

    if request.user.is_authenticated:
        page = 'login'
        return redirect('index')


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exsist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('snake')
        else:
            messages.error(request, 'Username OR passowrd is incorrect')


    return render(request, 'users/login_registration.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was successfully logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'

    countries = Country.objects.all()
    context = {'countries':countries}

    # cities = City.objects.all()
    # context = {'cities':cities}


    if request.method == 'POST':

        form = CustomuserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

    
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
           

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
        
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, 'User account was created!')

            return redirect('index')

    else:
        form = CustomuserCreationForm()
        profile_form = UserProfileForm()

    context = {'page': page, 'form': form, 'profile_form': profile_form, 'countries':countries, 'cities': cities}
    return render(request, 'users/login_registration.html', context)

# def updateProfile(request, pk):
#     userProfile = UserProfile.objects.get(id=pk)
#     profile_form = UserProfileForm(instance=userProfile)

#     if request.method == 'POST':
#         profile_form = UserProfileForm(request.POST, instance=userProfile)
#         if profile_form.is_valid():
#             profile_form.save()
#             return redirect('index')

#     context = {'profile_form': profile_form}
#     return render(request, 'users/edit-profile.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.userprofile
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {'form': form}
    return render(request, 'users/edit-profile.html', context)


@login_required(login_url="login")
def profile(request):
    username = request.user
    snakeHighScores = SnakeHighScore.objects.filter(username=username).order_by('-highScore')
    profiles = UserProfile.objects.all()

    context = {'profiles': profiles, 'snakeHighScores': snakeHighScores}
    return render(request, 'users/profiles.html', context)




# Test if I can delete the below:

def countries(request):
    countries = Country.objects.all()
    context = {'countries':countries}
    return render(request, 'users/login_registration.html', context)

def stateProvince(request):
    stateProvince = StateProvince.objects.all()
    context = {'stateProvince':stateProvince}
    return render(request, 'users/login_registration.html', context)

def cities(request):
    cities = City.objects.all()
    context = {'cities': cities}
    return render(request, 'users/login_registration.html', context)















