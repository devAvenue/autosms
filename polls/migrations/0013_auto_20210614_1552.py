# Generated by Django 3.2 on 2021-06-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20210614_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='numbers_of_phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('sms_kod', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('price_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='number_of_users',
        ),
    ]