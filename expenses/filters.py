
from django_filters import NumberFilter, CharFilter, DateTimeFilter, BooleanFilter, FilterSet, ChoiceFilter
from expenses.models import Expense
from django.db  import models
from django import forms
from django_filters import DateTimeFilter


def filter_not_empty(queryset, name, value):
    """
     Custom Filter to check if the Image Field in 
     Expense Object is empty or not
    """
    if value == 'false':
        return queryset.filter(image__exact="")
    else:
        return queryset.filter(image__regex="^(?!\s*$).+")



ADDRESSED_CHOICES = (
    ('true','Image Attached'),
    ('false','Image Not Attached'),
)

class ExpenseListFilter(FilterSet):
 
    #this filter is used to filter any substring in the name of the expense
    name__cont = CharFilter(field_name='name', lookup_expr='icontains')
    
    #this filter is used to filter expenses which are greater than equal to the given amount
    amount__gt = NumberFilter(field_name='amount', lookup_expr='gte')

    #this filter is used to filter expenses which are greater than equal to the given amount
    amount__lt = NumberFilter(field_name='amount', lookup_expr='lt')
 
    #this filter is used to filter expenses which have been created after the given date
    created__gt = DateTimeFilter(field_name='created', lookup_expr='gte')

    #this filter is used to filter expenses which have been created before the given date
    created__lt = DateTimeFilter(field_name='created', lookup_expr='lt')

    #this filter is used to filter expenses based on image attached or not
    image__exists = ChoiceFilter(method=filter_not_empty, choices=ADDRESSED_CHOICES, label='Status', field_name='image')


    class Meta:
        model = Expense
        fields = ('name', 'amount','created', 'image__exists')
        order_by = ['pk']


