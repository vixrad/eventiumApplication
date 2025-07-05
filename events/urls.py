from django.urls import path
from .views import EventsListView, EventDetailView, EventCreateView, EventEditView, EventDeleteView

urlpatterns = [
    path('', EventsListView.as_view(), name='events'),
    path('create/', EventCreateView.as_view(), name='create-event'),
    path('<int:pk>/details/', EventDetailView.as_view(), name='event-details'),
    path('<int:pk>/edit/', EventEditView.as_view(), name='edit-event'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='delete-event'),
]