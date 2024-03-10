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
    place = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    nr_tickets = models.IntegerField()


class Coupon(models.Model):
    coupon = models.CharField(max_length=200, blank=False, null=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    perc_discount = models.DecimalField(max_digits=5, decimal_places=2)
    price_discount = models.DecimalField(max_digits=10, decimal_places=2)


class Ticket(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    dt_buy = models.DateTimeField(default=timezone.now)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)
