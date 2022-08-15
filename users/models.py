from django.db import models
from django.contrib.auth.models import User
import uuid


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StateProvince(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")


    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    stateProvince = models.ForeignKey(StateProvince, on_delete=models.CASCADE, null=True, related_name="stateProvince")

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    stateProvince = models.ForeignKey(StateProvince, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return str(self.user)


