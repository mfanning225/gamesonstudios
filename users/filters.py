import django_filters
from django_filters import DateFilter, CharFilter

from snake.models import SnakeHighScore



class SnakeHighScoreFilter(django_filters.FilterSet):

    username = CharFilter(field_name='username', label='Username', lookup_expr='icontains')
    country = CharFilter(field_name='country', label='Country', lookup_expr='icontains')
    stateProvince = CharFilter(field_name='stateProvince', label='State/Province', lookup_expr='icontains')
    city = CharFilter(field_name='city', label='City', lookup_expr='icontains')

    class Meta:
        model = SnakeHighScore
        fields = ['username', 'country','stateProvince','city']

        #exclude = ['']
