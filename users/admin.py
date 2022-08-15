from atexit import register
from django.contrib import admin
# from .models import Profile
from .models import UserProfile, City, StateProvince, Country

    

admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(StateProvince)






