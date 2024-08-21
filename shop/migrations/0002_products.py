# Generated by Django 5.1 on 2024-08-11 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('cod_product', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_id', message='El ID del empleado solo puede contener números.', regex='^[0-9]*$')])),
                ('cant', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_id', message='El ID del empleado solo puede contener números.', regex='^[0-9]*$')])),
            ],
        ),
    ]