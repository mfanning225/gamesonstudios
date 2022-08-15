from django.forms import ModelForm
from .models import SnakeHighScore


class SnakeForm(ModelForm):
    class Meta:
        model = SnakeHighScore
        fields = ['highScore', 'username', 'city', 'stateProvince', 'country']


