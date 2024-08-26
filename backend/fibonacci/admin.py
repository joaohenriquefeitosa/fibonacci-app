from django.contrib import admin
from .models import FibonacciData

# Register your models here.
@admin.register(FibonacciData)
class FibonacciDataAdmin(admin.ModelAdmin):
    list_display = ('value', 'serie')