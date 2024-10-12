from django.db import models
from django.contrib.gis.db import models as gmodels
from rest_framework import serializers
from datetime import timedelta
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Author Name"))

    def __str__(self) -> str:
        return self.name

    @property
    def books_count(self):
        return self.books.count()

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Category Name"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name=_("Book Title"))
    category = models.ForeignKey(
        Category, related_name="books", on_delete=models.CASCADE, verbose_name=_("Category")
    )
    author = models.ForeignKey(
        Author, related_name="books", on_delete=models.CASCADE, verbose_name=_("Author")
    )
    price = models.PositiveIntegerField(verbose_name=_("Price"))
    is_available = models.BooleanField(default=True, verbose_name=_("Is Available"))

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class Library(gmodels.Model):
    name = models.CharField(verbose_name=_("Library Name"), max_length=100, unique=True)
    books = models.ManyToManyField(Book, blank=True, verbose_name=_("Books"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('Library')
        verbose_name_plural = _('Libraries')


class Branch(models.Model):
    location = gmodels.PointField(verbose_name=_("Location"))
    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name="branches", verbose_name=_("Library")
    )

    def __str__(self) -> str:
        return self.library.name

    class Meta:
        verbose_name = _('Branch')
        verbose_name_plural = _('Branches')


class LibraryTransaction(models.Model):
    user = models.ForeignKey(
        "accounts.Customer", on_delete=models.CASCADE, related_name="borrowed_books", verbose_name=_("User")
    )
    librarian = models.ForeignKey(
        'accounts.Librarian', on_delete=models.CASCADE, related_name='head_transactions', verbose_name=_("Librarian")
    )
    library = models.ForeignKey(
        Library, on_delete=models.CASCADE, related_name="transactions", verbose_name=_("Library")
    )
    books = models.ManyToManyField(Book, blank=True, through="BorrowReturnBook", verbose_name=_("Books"))
    name = models.CharField(max_length=10, choices=(('borrow', 'borrow'), ("purchase", 'purchase'), ('return', 'return')),
                            default='borrow', verbose_name=_("Transaction Type"))

    def __str__(self):
        return f"Transaction by {self.user.username}"

    class Meta:
        verbose_name = _('Library Transaction')
        verbose_name_plural = _('Library Transactions')


class BorrowReturnBook(models.Model):
    transaction = models.ForeignKey(
        LibraryTransaction, on_delete=models.CASCADE, related_name="books_transactions", verbose_name=_("Transaction")
    )
    book = models.ForeignKey(Book, related_name="books", on_delete=models.CASCADE, verbose_name=_("Book"))
    borrow_date = models.DateTimeField(default=timezone.now, verbose_name=_("Borrow Date"))
    return_date = models.DateTimeField(verbose_name=_("Return Date"))
    penalty = models.PositiveIntegerField(default=0, verbose_name=_("Penalty"))
    is_returned = models.BooleanField(default=False, verbose_name=_("Is Returned"))

    def clean(self) -> None:
        if not self.pk:
            if self.book.is_available:
                if self.return_date and self.return_date > self.borrow_date + timedelta(days=30):
                    raise serializers.ValidationError(
                        detail={"message": _("You can't specify return date more than one month of borrow date.")}
                    )
            else:
                raise serializers.ValidationError(detail={"message": _("Book is not available. We will confirm you when it's available.")})

        return super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('Borrow/Return Book')
        verbose_name_plural = _('Borrow/Return Books')
