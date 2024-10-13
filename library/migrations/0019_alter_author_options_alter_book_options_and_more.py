# Generated by Django 4.2.7 on 2024-10-13 00:20

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_customer_options_alter_librarian_options_and_more'),
        ('library', '0018_borrowreturnbook_is_returned'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='borrowreturnbook',
            options={'verbose_name': 'Borrow/Return Book', 'verbose_name_plural': 'Borrow/Return Books'},
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='library',
            options={'verbose_name': 'Library', 'verbose_name_plural': 'Libraries'},
        ),
        migrations.AlterModelOptions(
            name='librarytransaction',
            options={'verbose_name': 'Library Transaction', 'verbose_name_plural': 'Library Transactions'},
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Author Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.category', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_available',
            field=models.BooleanField(default=True, verbose_name='Is Available'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Book Title'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='library.book', verbose_name='Book'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='borrow_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Borrow Date'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='is_returned',
            field=models.BooleanField(default=False, verbose_name='Is Returned'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='penalty',
            field=models.PositiveIntegerField(default=0, verbose_name='Penalty'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='return_date',
            field=models.DateTimeField(verbose_name='Return Date'),
        ),
        migrations.AlterField(
            model_name='borrowreturnbook',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_transactions', to='library.librarytransaction', verbose_name='Transaction'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='library.library', verbose_name='Library'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ar',
            field=models.CharField(max_length=100, null=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(blank=True, to='library.book', verbose_name='Books'),
        ),
        migrations.AlterField(
            model_name='librarytransaction',
            name='books',
            field=models.ManyToManyField(blank=True, through='library.BorrowReturnBook', to='library.book', verbose_name='Books'),
        ),
        migrations.AlterField(
            model_name='librarytransaction',
            name='librarian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='head_transactions', to='accounts.librarian', verbose_name='Librarian'),
        ),
        migrations.AlterField(
            model_name='librarytransaction',
            name='library',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='library.library', verbose_name='Library'),
        ),
        migrations.AlterField(
            model_name='librarytransaction',
            name='name',
            field=models.CharField(choices=[('borrow', 'borrow'), ('purchase', 'purchase'), ('return', 'return')], default='borrow', max_length=10, verbose_name='Transaction Type'),
        ),
        migrations.AlterField(
            model_name='librarytransaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='accounts.customer', verbose_name='User'),
        ),
    ]
