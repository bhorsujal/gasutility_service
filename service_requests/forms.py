from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'description']

class MultipleFileInput(forms.widgets.FileInput):
    allow_multiple_selected = True  # Allows selecting multiple files

class AttachmentForm(forms.Form):
    files = forms.FileField(
        widget=MultipleFileInput(attrs={'multiple': True, 'class': 'form-control'}),
        required=False  # Optional field for attachments
    )
