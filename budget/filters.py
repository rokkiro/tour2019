import django_filters
from budget.models import Money

class MoneyFilter(django_filters.FilterSet):

    class Meta:
        model = Money
        fields = ('category', 'city')