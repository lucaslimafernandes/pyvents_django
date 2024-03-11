from django.contrib import admin
from .models import Coupon, Event, Ticket 

# Register your models here.

admin.site.register([Coupon, Event, Ticket])
