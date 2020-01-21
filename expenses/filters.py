
from django_filters import NumberFilter, CharFilter, DateTimeFilter, BooleanFilter, FilterSet
from expenses.models import Expense
from django.db  import models
from django import forms
from django_filters import DateTimeFilter


def filter_not_empty(queryset, name, value):
    #lookup = '__'.join([name, exact])
    if value is False:
        return queryset.filter(image__exact="")
    else:
        return queryset.filter(image__regex="^(?!\s*$).+")


class ExpenseListFilter(FilterSet):
    name__cont = CharFilter(field_name='name', lookup_expr='icontains')
    amount__gt = NumberFilter(field_name='amount', lookup_expr='gte')
    amount__lt = NumberFilter(field_name='amount', lookup_expr='lte')
    created__gt = DateTimeFilter(field_name='created', lookup_expr='gte')
    created__lt = DateTimeFilter(field_name='created', lookup_expr='lt')
    image__exists = BooleanFilter(field_name='image', method=filter_not_empty) 

    class Meta:
        model = Expense
        #exclude = ['image']
        fields = ('name', 'amount','created', 'image__exists')
        #fields = {
        #    'name': ['exact'],
        #    'amount':['exact','lte', 'gte'],
        #    'created' : ['exact', 'year__gt'],
        #}
        order_by = ['pk']
        #filter_overrides = {
        #     models.ImageField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }


