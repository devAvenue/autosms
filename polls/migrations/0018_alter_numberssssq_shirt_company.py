# Generated by Django 3.2 on 2021-06-14 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_alter_numberssssq_shirt_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberssssq',
            name='shirt_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.company'),
        ),
    ]
