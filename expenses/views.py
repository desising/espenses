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
from .utils import PagedFilteredTableView
from django.db.models import Avg, Count, Min, Sum
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.contrib.auth.forms import UserCreationForm

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



class ExpenseListView(LoginRequiredMixin, PagedFilteredTableView):
    login_url = '/expenses/login/'
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
        a = Expense.objects.filter(user=self.request.user).aggregate(Sum('amount'))
        if a is None:
            return 0
        return a

    def get_queryset(self):
        qs = super(ExpenseListView, self).get_queryset().filter(user=self.request.user)
        #qs1 = Expense.objects.filter(user=self.request.user)
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
    login_url = '/expenses/login/'
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
    login_url = '/expenses/login/'
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
    login_url = '/expenses/login/'
    model = Expense
    name = 'expense-detail'
    template_name = 'expense_detail.html'
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        else:
            return Expense.objects.none()


class ExpenseDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/expenses/login/'
    model = Expense
    name = 'expense-delete'
    template_name = 'expense_delete.html'
    success_url = reverse_lazy('expense-list')
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user)
        else:
            return Expense.objects.none()
    
