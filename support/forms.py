from django import forms
from service_requests.models import ServiceRequest

class ServiceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status']