from django.db import models
from django.contrib.gis.db import models as gmodels
from django.contrib.gis.db.models.functions import Distance
from django.contrib.auth.models import AbstractUser
from library.models import Branch
from django.contrib.gis.measure import D
from django.contrib.auth.models import Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from .managers import *
from phonenumber_field.modelfields import PhoneNumberField
from library.models import BorrowReturnBook


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):

        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(email=self.email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("role", "librarian")
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class User(
    AbstractUser,
    gmodels.Model,
):
    location = gmodels.PointField(_("User Location"), null=True, blank=True)
    email = models.EmailField(unique=True)
    role = models.CharField(
        choices=(("customer", "customer"), ("librarian", "librarian")),
        default="customer",
    )
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    phone = PhoneNumberField(blank=True)


class Customer(User):
    objects = CustomerManager()

    class Meta:
        proxy = True
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def get_borrowed_books_count(self):

        return BorrowReturnBook.objects.filter(
            transaction__user=self, is_returned=False
        ).count()

    def get_nearby_libraries(self):
        if not self.location:
            return None

        nearby_libraries = (
            Branch.objects.filter(location__distance_lte=(self.location, D(km=1)))
            .annotate(distance=Distance("location", self.location))
            .order_by("distance")
        )
        libraries_list = []
        for branch in nearby_libraries:
            libraries_list.append(
                {
                    "name": branch.library.name,
                    "location": {
                        "longitude": branch.location.x,
                        "latitude": branch.location.y,
                    },
                    "distance_km": branch.distance.km,
                }
            )

        return libraries_list

    def save(self, *args, **kwargs):
        self.role = "customer"

        return super().save(*args, **kwargs)


class Librarian(User):
    library = models.ForeignKey(
        "library.Library", on_delete=models.CASCADE, related_name="librarians"
    )

    class Meta:
        verbose_name = _("Librarian")
        verbose_name_plural = _("Librarians")

    def save(self, *args, **kwargs):
        self.role = "librarian"

        return super().save(*args, **kwargs)
