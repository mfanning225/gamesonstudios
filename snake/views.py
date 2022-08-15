from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import SnakeHighScore, UserProfile
from .forms import SnakeForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, date, timedelta, time
import pytz


@login_required(login_url="login")
def snake(request):
    username = request.user

    
    
    try:
        time_now_now = SnakeHighScore.objects.filter(username=username).latest('time_now')

        tz = pytz.timezone("America/New_York")
        today = datetime.now(tz).date()      
        midnight = tz.localize(datetime.combine(today, time(0, 0)), is_dst=None)
        fmt = '%Y-%m-%d %H'
        mid = midnight.astimezone(pytz.utc).strftime(fmt)
        print(mid)

    except SnakeHighScore.DoesNotExist:
        time_now_now = None
        mid = None


    high_score_form = SnakeForm()
    user_profile = UserProfile.objects.all()


    if request.method == 'POST':
    
    
        high_score_form = SnakeForm(request.POST, request.FILES)
        if high_score_form.is_valid():
            high_score_form.user = request.user

            high_score_form.save()
            return redirect('profile')
            #return render(request, 'users/profiles.html')
        
            
    context = {'high_score_form': high_score_form, 'user_profile': user_profile, 'time_now_now': time_now_now,'mid': mid}
    return render(request, 'snake/snake.html', context)






