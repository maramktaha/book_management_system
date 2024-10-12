from django_cron import CronJobBase, Schedule
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
from .models import BorrowReturnBook

class SendReminderEmailsCronJob(CronJobBase):
    RUN_EVERY_MINS = 24*60

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'library.send_reminder_emails'  

    def do(self):
        today = timezone.now().date()
       

        upcoming_due_transactions = BorrowReturnBook.objects.filter(
            is_returned=False,
            return_date__date__range=[today, today + timedelta(days=3)]
        )

        for book in upcoming_due_transactions:
            user = book.transaction.user
            return_date = book.return_date.date()
            days_remaining = (return_date - today).days

         
            subject = 'Reminder: Book Return Due Soon'
            message = f'Dear {user.first_name},\n\nYou have borrowed books that are due to be returned on {return_date}.\n'
            message += f'You have {days_remaining} day(s) left to return the books.\n\n'
            message += 'Please make sure to return them on time to avoid penalties.\n\nThank you!'

            # Send the email
            send_mail(
                subject,
                message,
                'maram.ktaha@Gmail.com', 
                [user.email], 
                fail_silently=False,
            )
