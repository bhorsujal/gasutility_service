from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from service_requests.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('support/', include('support.urls')),
    path('service/', include('service_requests.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)