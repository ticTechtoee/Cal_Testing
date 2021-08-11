from django.contrib import admin
from range.models import price_range
from range.models import update_price
# Register your models here.

admin.site.register(price_range)
admin.site.register(update_price)
