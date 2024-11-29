from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ServiceRequestForm, AttachmentForm
from .models import ServiceRequest, Attachment

# Create your views here.

class ServiceRequestCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ServiceRequestForm()
        attachment_form = AttachmentForm()
        return render(request, 'service_requests/request_form.html', {'form': form, 'attachment_form': attachment_form})

    def post(self, request):
        form = ServiceRequestForm(request.POST)
        attachment_form = AttachmentForm(request.POST, request.FILES)
        files = request.FILES.getlist('files')
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            for i in files: # an entry for every file in attachment table
                Attachment.objects.create(service_request=service_request, file=i)
            return redirect('service_requests:request_detail', pk=service_request.pk)
        return render(request, 'service_requests/request_form.html', {'form': form, 'attachment_form': attachment_form})

class ServiceRequestDetailView(LoginRequiredMixin, View):
    def get(self, request, pk):
        service_request = get_object_or_404(ServiceRequest, pk=pk, customer=request.user)
        return render(request, 'service_requests/request_detail.html', {'service_request': service_request})

class ServiceRequestListView(LoginRequiredMixin, View):
    def get(self, request):
        requests = ServiceRequest.objects.filter(customer=request.user).order_by('-created_at') # desc
        return render(request, 'service_requests/request_list.html', {'requests': requests})

def home_view(request):
    if request.user.is_authenticated:
        if request.user.role in ['support', 'admin']:
            return redirect('support:dashboard')
        return redirect('service_requests:request_list')  # Redirect logged-in "customers" to "My Requests"
    else:
        return render(request, 'home.html')  # Render public home page for logged-out users