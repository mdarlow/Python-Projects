from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    objects = models.Manager()

    def __str__(self):
        return self.title
