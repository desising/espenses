from django.test import TestCase
from expenses.models import Expense
from django.contrib.auth.models import User

#class ExpenseModelTest(TestCase):
#    def setup(self):
#        Expense.objects.create(name="Dinner at Taj", amount="2000")

#from django.test import TestCase


class ExpenseModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='raj', password='abcd1234')
        self.expense = Expense.objects.create(name="Dinner at Taj", user=user, amount=2000)


    def test_str_representation(self):
        self.assertEqual(str(self.expense), self.expense.name)
        
    def test_absolute_url(self):
        #print(self.expense.get_absolute_url())
        self.assertEqual(self.expense.get_absolute_url(), "/expenses/my/")    
