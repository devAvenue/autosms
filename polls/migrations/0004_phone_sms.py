# Generated by Django 3.2.4 on 2021-06-11 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210612_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='phone_sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('sms', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Смс',
                'verbose_name_plural': 'Смс',
            },
        ),
    ]