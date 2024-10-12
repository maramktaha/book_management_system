from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import LibraryTransaction
from django.core.mail import send_mail
from django.template.loader import render_to_string
from rest_framework import serializers
from django.db.models.signals import m2m_changed


@receiver(post_save, sender=LibraryTransaction)
def send_email_upon_borrow(sender, instance=None, created=True, **kwargs):
    if created:
        instance.books.update(is_available=False)

        if instance.name == "borrow":

            context = {
                "user_name": instance.user.username,
                "books": instance.books_transactions.all(),
            }

            html_content = render_to_string("borrow_book_template.html", context)

          
            subject = "Borrowing Confirmation"
            from_email = "maram.ktaha@gmail.com"

        
            send_mail(
                subject,
                "",
                from_email,
                [instance.user.email],
                html_message=html_content,
            )


@receiver(m2m_changed, sender=LibraryTransaction.books.through)
def check_borrowed_books_limit(sender, instance, action, **kwargs):

    if action == "pre_add":
        user = instance.user
        borrowed_books_count = user.get_borrowed_books_count()
        new_books_count = len(kwargs.get("pk_set", []))

        if borrowed_books_count + new_books_count > 3:
            raise serializers.ValidationError(
                detail={
                    "message": "You can't borrow more than 3 books. Please return at least 1 before borrowing more."
                }
            )
