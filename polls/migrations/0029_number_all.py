# Generated by Django 3.2 on 2021-07-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0028_numberssssq_bool_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_all',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shirt_sizes', models.CharField(choices=[('KNK', 'Канада'), ('USA', 'США'), ('RUS', 'Россия'), ('NDN', 'Нидерланды'), ('FRF', 'Франция'), ('ISI', 'Испания'), ('ITI', 'Италия'), ('AVA', 'Австрия'), ('UKU', 'Англия'), ('GER', 'Германия')], default='USA', max_length=5)),
                ('hours_sizes', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four'), ('five', 'five')], default='one', max_length=5)),
                ('days_sizes', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three'), ('four', 'four')], default='one', max_length=5)),
                ('weeks_sizes', models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three')], default='one', max_length=5)),
                ('monsday_sizes', models.CharField(choices=[('one', 'one'), ('two', 'two')], default='one', max_length=5)),
                ('number_phone', models.CharField(max_length=100)),
                ('bool_number', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Все номера',
                'verbose_name_plural': 'Все номера',
            },
        ),
    ]