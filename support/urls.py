from django.urls import path
from .views import (SupportDashboardView, 
                    RequestListView, 
                    RequestDetailView, 
                    RequestUpdateView)

app_name = 'support'

urlpatterns = [
    path('', SupportDashboardView.as_view(), name='dashboard'),
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('requests/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('requests/<int:pk>/update/', RequestUpdateView.as_view(), name='request_update'),
]