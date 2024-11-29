from django.contrib import admin
from .models import ServiceRequest, Attachment

# Register your models here.
admin.site.register(ServiceRequest)
admin.site.register(Attachment)