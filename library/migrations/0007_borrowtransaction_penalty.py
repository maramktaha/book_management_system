# Generated by Django 5.1.1 on 2024-10-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_remove_borrowtransaction_library'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowtransaction',
            name='penalty',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
