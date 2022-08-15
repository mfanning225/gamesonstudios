from django.shortcuts import render
from .filters import SnakeHighScoreFilter
from snake.models import SnakeHighScore
#from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url="login")
def leaderboard(request):

    snakeHighScores = SnakeHighScore.objects.all().order_by('-highScore')

    myFilter = SnakeHighScoreFilter(request.GET, queryset=snakeHighScores)
    snakeHighScores = myFilter.qs

    context = {'snakeHighScores':snakeHighScores,'myFilter': myFilter}

    return render(request, 'leaderboard/leaderboard.html', context)

