from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.urls import reverse

# Create your models here.
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=False, default='')
    amount = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)

    def get_absolute_url(self):
        return reverse('expense-list')

