from django.db import models
from users.models import UserProfile
from django.contrib.auth.models import User
import uuid
from datetime import datetime, timedelta, timezone
# Create your models here.
from django.utils import timezone


class SnakeHighScore(models.Model):
    #userProfile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    stateProvince = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    highScore = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    time_now = models.DateTimeField(default=timezone.now)




    class Meta:
        get_latest_by = ['time_now']


    def __str__(self):
        return str(self.username)



