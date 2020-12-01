import django_filters
from .models import Order
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_ordered', lookup_expr='gte')
    end_date = DateFilter(field_name='date_ordered', lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['date_ordered', 'name']
