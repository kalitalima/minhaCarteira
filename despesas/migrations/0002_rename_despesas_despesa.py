# Generated by Django 5.0.6 on 2024-05-18 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0001_initial'),
        ('integrantes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Despesas',
            new_name='Despesa',
        ),
    ]
