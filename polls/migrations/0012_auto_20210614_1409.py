# Generated by Django 3.2 on 2021-06-14 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_numberssssq_shirt_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='number_of_users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=100)),
                ('sms_kod', models.CharField(max_length=100)),
                ('price_number', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='numberssssq',
            name='shirt_company',
            field=models.CharField(choices=[('lol', 'lol'), ('kek', 'kek'), ('popit', 'popit'), ('simpldimpl', 'simpldimpl'), ('apple', 'apple')], default='App', max_length=15),
        ),
    ]
