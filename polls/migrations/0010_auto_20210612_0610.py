# Generated by Django 3.2.4 on 2021-06-12 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_phone_sms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='numberssssq',
            name='price_rubsq',
        ),
        migrations.RemoveField(
            model_name='numberssssq',
            name='price_usasq',
        ),
    ]