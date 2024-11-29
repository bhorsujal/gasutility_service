from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from service_requests.models import ServiceRequest
from .models import ActivityLog
from .forms import ServiceRequestUpdateForm

# Create your views here.

class SupportDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'support/dashboard.html'

    def test_func(self):
        return self.request.user.role in ['admin', 'support']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_requests'] = ServiceRequest.objects.count()
        context['open_requests'] = ServiceRequest.objects.filter(status__in=['pending', 'in_progress']).count()
        return context

class RequestListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ServiceRequest
    template_name = 'support/request_list.html'
    paginate_by = 20

    def test_func(self):
        return self.request.user.role in ['admin', 'support']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.order_by('-created_at')

class RequestDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ServiceRequest
    template_name = 'support/request_detail.html'

    def test_func(self):
        return self.request.user.role in ['admin', 'support']

class RequestUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ServiceRequest
    form_class = ServiceRequestUpdateForm
    template_name = 'support/request_update.html'
    success_url = reverse_lazy('support:dashboard')

    def test_func(self):
        return self.request.user.role in ['admin', 'support']

    def form_valid(self, form):
        response = super().form_valid(form)
        # Log the activity (create)
        ActivityLog.objects.create(
            service_request=self.object,
            action='Updated status to {}'.format(self.object.get_status_display()),
            performed_by=self.request.user
        )
        return response