# Generated by Django 3.2 on 2021-06-14 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0016_numberssssq_shirt_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numberssssq',
            name='shirt_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.company', verbose_name='name_company'),
        ),
    ]