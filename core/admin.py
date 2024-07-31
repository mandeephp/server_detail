from django.contrib import admin

from core.models import ServerMetric, ORMS

# Register your models here.
admin.site.register(ServerMetric)
admin.site.register(ORMS)