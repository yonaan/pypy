from django.contrib import admin
from .models import MasterSensor,MasterThreshold,Temperature_Data
# Register your models here.

admin.site.register(MasterSensor)
admin.site.register(MasterThreshold)
admin.site.register(Temperature_Data)