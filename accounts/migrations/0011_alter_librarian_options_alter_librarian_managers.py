# Generated by Django 4.2.7 on 2024-10-11 20:42

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_delete_librarian_librarian'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='librarian',
            options={'verbose_name': 'Librarian'},
        ),
        migrations.AlterModelManagers(
            name='librarian',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
