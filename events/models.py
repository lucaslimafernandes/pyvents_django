from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    event_date = models.DateTimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    nr_tickets = models.IntegerField()


