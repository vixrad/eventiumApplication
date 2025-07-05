from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('events/', include('events.urls')),
    path('organizer/', include('organizers.urls')),
]
