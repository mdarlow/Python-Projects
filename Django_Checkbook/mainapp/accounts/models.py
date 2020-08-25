from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    starting_balance = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.first_name
