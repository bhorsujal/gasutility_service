from django.db import models
from django.conf import settings
from django.utils.timezone import now

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    SERVICE_TYPE_CHOICES = [
        ('New Service Connection', 'New Service Connection'),
        ('Service Disconnection', 'Service Disconnection'),
        ('Billing and Payments', 'Billing and Payments'),
        ('Meter Issues', 'Meter Issues'),
        ('Gas Leaks or Safety Concerns', 'Gas Leaks or Safety Concerns'),
        ('Maintenance Requests', 'Maintenance Requests'),
        ('Account Updates', 'Account Updates'),
        ('Reconnection of Service', 'Reconnection of Service'),
        ('Energy Efficiency Advice', 'Energy Efficiency Advice'),
        ('Complaints', 'Complaints'),
        ('General Inquiries', 'General Inquiries'),
        ('Appointment Scheduling', 'Appointment Scheduling'),
        ('Moving Services', 'Moving Services'),
        ('Promotions and Offers', 'Promotions and Offers'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=255, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status in ['resolved', 'closed'] and self.resolved_at is None:
            self.resolved_at = now()
        super(ServiceRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f"#{self.id} - {self.service_type}"


# Attachments for requests
class Attachment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for service id: {self.service_request.id}"