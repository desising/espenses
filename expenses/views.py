from django.views.generic.list import ListView
from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .tables import ExpenseTable
from .filters import ExpenseListFilter
from .forms import ExpenseListFormHelper
from expenses.models import Expense 
from django_tables2 import RequestConfig
from django.db.models.query_utils import Q
from .utils import FilteredTableView
from django.db.models import Avg, Count, Min, Sum
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    """
     View for user registration Page
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



class ExpenseListView(LoginRequiredMixin, FilteredTableView):
    """
       View for Seeing the list of expenses in a paginated and tabular form
       It inherently used ListView. Login is required to access this view
       
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Expense
    paginate_by = 5
    template_name = 'expense_list.html'
    name = 'expense-list'
    context_object_name = 'expense'
    ordering = ['-id']
    table_class = ExpenseTable
    filter_class = ExpenseListFilter
    formhelper_class = ExpenseListFormHelper

    def total_expense(self):
        """
           This function returns the total expenditure made in by a particular user
        """
        a = Expense.objects.filter(user=self.request.user).aggregate(Sum('amount'))
        if a is None:
            return 0
        return a

    def get_queryset(self):
        """
            Gets the query list from the filtered form and also added the filter for logged in user
        """
        qs = super(ExpenseListView, self).get_queryset().filter(user=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ExpenseListView, self).get_context_data(**kwargs)
        context['nav_customer'] = True
        context['total_expense'] = self.total_expense()['amount__sum']
        search_query = self.get_queryset()
        table = ExpenseTable(search_query)
        RequestConfig(self.request, paginate={'per_page': 5}).configure(table)
        context['table'] = table
        return context



class ExpenseCreateView(LoginRequiredMixin, CreateView):
    """
      This view is used to create or add an expense by the logged in user.
      Login is mandatory for accessing this
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Expense
    name = 'expense-create'
    template_name = 'expense_form.html'
    fields = ('name', 'amount', 'image')
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('expense-list'))


class ExpenseUpdateView(LoginRequiredMixin, UpdateView):
    """
      This is view is used by the logged in user to update an existing expense
      Login is mandatory for accessing this view
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Expense
    name = 'expense-update'
    template_name = 'expense_update_form.html'
    fields = ('name', 'amount', 'image')
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        else:
            return Expense.objects.none()


class ExpenseDetailView(LoginRequiredMixin, DetailView):
    """
     This view is used by the logged in user see details of an espense
     including name, created timestamp, image if any and amount
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Expense
    name = 'expense-detail'
    template_name = 'expense_detail.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        else:
            return Expense.objects.none()


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    """
     This view is used by the logged in user to delete an expense
     Login is mandatory to perform this operation
    """
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Expense
    name = 'expense-delete'
    template_name = 'expense_delete.html'
    success_url = reverse_lazy('expense-list')
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        else:
            return Expense.objects.none()
    
