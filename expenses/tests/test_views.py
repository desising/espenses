from PIL import Image
from io import StringIO, BytesIO
from django.test import TestCase
from expenses.models import Expense
from expenses import views
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.files.base import ContentFile


class RegisterViewTest(TestCase):
    
    def test_user_registration(self):
        res = self.client.post('/expenses/register/', {'username':"raj123", 'password1': "abcd1234#", 'password2':"abcd1234#"}, follow=True)
        self.assertEqual(res.status_code,200)
        self.user = User.objects.get(username="raj123")
        self.assertEqual(self.user.username, "raj123")

    def test_user_login_after_registration(self):
        res = self.client.post('/login/', {'username':"raj123", 'password':'abcd1234#'})
        self.assertEqual(res.status_code,200)


class ExpenseListViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='raj', password='abcd1234')
        image_file = BytesIO()
        Image.new("RGBA",(200,200),(0,0,255,0)).save(image_file, 'png')
        image_file.seek(0)
        self.image = ContentFile(image_file.read(), 'test.png')
        self.id = Expense.objects.create(name="Dinner", amount="2000", user=self.user, image=self.image).pk

    def test_list_expense_redirection_to_login_page(self):
        expected_redirection_url = '/login/?redirect_to=%2Fexpenses%2Fmy%2F'
        res = self.client.get('/expenses/my/', follow=True)
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_list_expense_after_login(self):
        self.client.login(username='raj', password='abcd1234')
        res = self.client.get('/expenses/my/', follow=True)
        self.assertEqual(res.status_code,200)


    
class ExpenseCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='raj', password='abcd1234')
        image_file = BytesIO()
        Image.new("RGBA",(200,200),(0,0,255,0)).save(image_file, 'png')
        image_file.seek(0)
        self.image = ContentFile(image_file.read(), 'test.png')

    def test_create_expense_redirection_to_login_page(self):
        res = self.client.post('/expenses/create/', {"name":"Dinner", "amount":200012,"image":self.image, "user":self.user}, follow=True)
        expected_redirection_url = '/login/?redirect_to=/expenses/create/'
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_create_expense_after_login(self):
        self.client.login(username=self.user.username, password='abcd1234')
        res = self.client.post('/expenses/create/', {"name":"Dinner", "amount":200012,"image":self.image, "user":self.user}, follow=True)
        self.assertEqual(res.status_code, 200)
        expenseObj = Expense.objects.get(name="Dinner")
        self.assertEqual(expenseObj.amount,200012)
        self.assertEqual(expenseObj.user.username, self.user.username)


class ExpenseUpdateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="raj", password="abcd1234")
        image_file = BytesIO()
        Image.new("RGBA",(200,200),(0,0,255,0)).save(image_file, 'png')
        image_file.seek(0)
        self.image = ContentFile(image_file.read(), 'test.png') 
        self.id = Expense.objects.create(name="Dinner", amount="2000", user=self.user, image=self.image).pk

    def test_edit_expense_redirection_to_login_page(self):
        expected_redirection_url = '/login/?redirect_to=%2Fexpenses%2F' + str(self.id)+'%2Fedit'
        res = self.client.post('/expenses/'+str(self.id)+'/edit',{"name":"Dinner123","amount":200012,"user":self.user},follow=True)
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_edit_expense_after_login_name__amount_update(self):
        self.client.login(username=self.user.username, password='abcd1234')
        res = self.client.post('/expenses/'+str(self.id)+'/edit', {"name":"Dinner_mod", "amount":200012}, follow=True)
        self.assertEqual(res.status_code, 200)
        expenseObj = Expense.objects.get(pk=self.id)
        self.assertEqual(expenseObj.name,'Dinner_mod')
        self.assertEqual(expenseObj.amount, 200012)


class ExpenseDetailViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='raj', password='abcd1234')
        image_file = BytesIO()
        Image.new("RGBA",(200,200),(0,0,255,0)).save(image_file, 'png')
        image_file.seek(0)
        self.image = ContentFile(image_file.read(), 'test.png')
        self.id = Expense.objects.create(name="Dinner", amount="2000", user=self.user, image=self.image).pk

    def test_detail_expense_redirection_to_login_page(self):
        expected_redirection_url = '/login/?redirect_to=%2Fexpenses%2F' + str(self.id)+'%2F'
        res = self.client.get('/expenses/'+str(self.id)+'/', follow=True)
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_detail_expense_after_login(self):
        self.client.login(username='raj', password='abcd1234')
        res = self.client.get('/expenses/'+str(self.id)+'/', follow=True)
        self.assertEqual(res.status_code,200)


class ExpenseDeleteViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='raj', password='abcd1234')
        image_file = BytesIO()
        Image.new("RGBA",(200,200),(0,0,255,0)).save(image_file, 'png')
        image_file.seek(0)
        self.image = ContentFile(image_file.read(), 'test.png')
        self.id = Expense.objects.create(name="Dinner", amount="2000", user=self.user, image=self.image).pk
     
    def test_delete_expense_redirection_to_login_page(self):
        expected_redirection_url = '/login/?redirect_to=%2Fexpenses%2F' + str(self.id)+'%2Fdelete'
        res = self.client.post('/expenses/'+str(self.id)+'/delete', follow=True)
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_delete_expense_after_login(self):
        self.client.login(username=self.user.username, password='abcd1234')
        expected_redirection_url = '/login/?redirect_to=%2Fexpenses%2F' + str(self.id)+'%2Fdelete'
        res = self.client.post('/expenses/'+str(self.id)+'/delete', follow=True)
        expected_redirection_url = '/expenses/my/'
        self.assertRedirects(res, expected_redirection_url, status_code=302, target_status_code=200, msg_prefix='', fetch_redirect_response=True)
        
