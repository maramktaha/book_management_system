# Generated by Django 4.2.7 on 2024-10-09 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0009_remove_library_location_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='name_ar',
            field=models.CharField(max_length=100, null=True, verbose_name='Library Name'),
        ),
        migrations.AddField(
            model_name='library',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Library Name'),
        ),
    ]
