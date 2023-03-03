from ckeditor.fields import RichTextField
from django.db import models
from dateutil.rrule import *
from dateutil.rrule import DAILY, WEEKLY, MONTHLY, YEARLY
from dateutil.parser import *

FREQUENCY_CHOICES = [
    (DAILY, 'Daily'),
    (WEEKLY, 'Weekly'),
    (MONTHLY, 'Monthly'),
    (YEARLY, 'yearly'),
]

class Calendar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(null=False, blank=False, unique=True, verbose_name='Slug')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    Debut = models.DateTimeField(null=True, default=None)
    Fin = models.DateTimeField(null=True, default=None)
    location = models.CharField(max_length=255)
    description = RichTextField(null=True)
    category = models.ForeignKey(Calendar, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recurrency = models.BooleanField(default=False)
    rrule = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.PositiveSmallIntegerField(choices=FREQUENCY_CHOICES, default=DAILY)
    count = models.PositiveSmallIntegerField(default=1)
    interval = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        choice = [
            (0, 'YEARLY'),
            (1, 'MONTHLY'),
            (2, 'WEEKLY'),
            (3, 'DAILY'),
        ]
        self.rrule = "FREQ={};DTSTART={};INTERVAL={};COUNT={}".format(
            choice[self.frequency][1], self.Debut.strftime("%Y%m%dT%H%M%S"), self.interval, self.count
        )
        super().save(*args, **kwargs)
