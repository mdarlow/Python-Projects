from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    starting_balance = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.first_name


TYPE_CHOICES = {
    ("deposit", "deposit"),
    ("withdrawal", "withdrawal"),
}


class Transaction(models.Model):
    date = models.CharField(max_length=60, default="", blank=True, null=False)
    type = models.CharField(max_length=60, choices=TYPE_CHOICES)
    amount = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    description = models.TextField(max_length=300, default="", blank=True)
    application = models.IntegerField(max_length=30, default="", blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.amount
