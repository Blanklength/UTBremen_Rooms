from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Room)
admin.site.register(DeviceCategory)
admin.site.register(DeviceType)
admin.site.register(Device)
admin.site.register(Location)
admin.site.register(OtherEquipment)
