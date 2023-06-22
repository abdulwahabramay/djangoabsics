from django.contrib import admin
from .models import *
# Register your models here.
class VegeAdmin(admin.ModelAdmin):
    list_display = ('receipe_name', 'receipe_description', 'receipe_image')
admin.site.register(Receipe,VegeAdmin)