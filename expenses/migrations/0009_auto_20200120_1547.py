# Generated by Django 2.2.9 on 2020-01-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_auto_20200120_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
