
from django_filters import NumberFilter, CharFilter, DateTimeFilter, BooleanFilter, FilterSet
from expenses.models import Expense
from django.db  import models
from django import forms
from django_filters import DateTimeFilter


def filter_not_empty(queryset, name, value):
    """
     Custom Filter to check if the Image Field in 
     Expense Object is empty or not
    """
    if value is False:
        return queryset.filter(image__exact="")
    else:
        return queryset.filter(image__regex="^(?!\s*$).+")


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
    image__exists = BooleanFilter(field_name='image', method=filter_not_empty) 

    class Meta:
        model = Expense
        fields = ('name', 'amount','created', 'image__exists')
        order_by = ['pk']


