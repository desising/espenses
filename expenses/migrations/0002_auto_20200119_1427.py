# Generated by Django 2.2.9 on 2020-01-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.ImageField(default='post.jpg', upload_to='images/'),
        ),
    ]
