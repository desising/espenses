import django_tables2 as tables
from django_tables2.utils import A
from .models import Expense

class ExpenseTable(tables.Table):
    """
       This class is used to provide link for expense 
       entries in the given table
    """
    name = tables.LinkColumn('expense-detail', args=[A('pk')])
    amount = tables.LinkColumn('expense-detail', args=[A('pk')])
    created = tables.LinkColumn('expense-detail', args=[A('pk')])
    
    class Meta:
        model = Expense
        per_page = 5
        fields = ('name', 'amount', 'created', 'image')
        attrs = {"class":"table-striped table-bordered"}
        empty_text = "There are no text matching the search criteria"
