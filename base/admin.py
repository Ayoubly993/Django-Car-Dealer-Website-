from django.contrib import admin
from .models import *
# Register your models here.
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 4

class CarAdmin(admin.ModelAdmin):
    inlines = [ CarImageInline, ]

admin.site.register(Car, CarAdmin)
