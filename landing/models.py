from django.db import models

# Create your models here.
class Landing(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name
