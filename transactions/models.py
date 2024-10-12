from django.contrib.auth.models import AbstractUser
from django.db import models

from transactions.constants import TRANSACTION_TYPES, CATEGORIES


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    Fields:
    - username, password, email (inherited)
    - first_name: User's first name
    - last_name: User's last name
    - telephone: Unique phone number for the user
    """
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    telephone = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField(blank=True)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} on {self.date}"