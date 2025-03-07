# Generated by Django 4.2.7 on 2024-10-11 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_librarytransaction_name'),
        ('accounts', '0009_user_phone_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Librarian',
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarians', to='library.library')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('accounts.user',),
        ),
    ]
