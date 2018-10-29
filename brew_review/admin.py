from django.contrib import admin
from .models import Brewery, Review

# Register your models here.

admin.site.register(Brewery)
admin.site.register(Review)