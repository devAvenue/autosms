# Generated by Django 3.2 on 2021-06-14 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_alter_numbers_of_phone_sms_kod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numbers_of_phone',
            name='sms_kod',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
