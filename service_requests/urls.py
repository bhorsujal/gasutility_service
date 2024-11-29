from django.urls import path
from .views import (ServiceRequestCreateView, 
                    ServiceRequestDetailView, 
                    ServiceRequestListView)

app_name = 'service_requests'

urlpatterns = [
    path('requests/', ServiceRequestListView.as_view(), name='request_list'),
    path('requests/new/', ServiceRequestCreateView.as_view(), name='request_create'),
    path('requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='request_detail'),
]