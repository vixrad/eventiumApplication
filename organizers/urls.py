from django.urls import path
from .views import CreateOrganizerView, OrganizerDetailView, OrganizerEditView, OrganizerDeleteView

urlpatterns = [
    path('create/', CreateOrganizerView.as_view(), name='create-organizer'),
    path('details/', OrganizerDetailView.as_view(), name='details-organizer'),
    path('edit/', OrganizerEditView.as_view(), name='edit-organizer'),
    path('delete/', OrganizerDeleteView.as_view(), name='delete-organizer'),
]