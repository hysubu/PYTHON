from django.contrib import admin
from app1.models import Data

# Register your models here.
@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['SrNo','Name','Gmail','Age','Add']
