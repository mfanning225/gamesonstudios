from django.contrib import admin
from .models import SnakeHighScore

class SnakeHighScores(admin.ModelAdmin):
    list_display = ('username','highScore','country', 'stateProvince', 'city')


admin.site.register(SnakeHighScore, SnakeHighScores)
