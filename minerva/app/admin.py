from django.contrib import admin
from app.models import ApplianceClass, ApplianceType, ApplianceUsage

# Register your models here.

admin.site.register(ApplianceClass)
admin.site.register(ApplianceType)
admin.site.register(ApplianceUsage)
