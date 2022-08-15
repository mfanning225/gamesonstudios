from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('playarcade.urls')),
    path('landing/', include('landing.urls')),
    path('snake/', include('snake.urls')),
    path('users/', include('users.urls')),
    path('leaderboard/', include('leaderboard.urls')),
    path('admin/', admin.site.urls),
]
