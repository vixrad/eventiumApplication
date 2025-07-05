from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from events.models import Event
from organizers.models import Organizer
from organizers.forms import OrganizerCreateForm, OrganizerEditForm

class CreateOrganizerView(CreateView):
    model = Organizer
    form_class = OrganizerCreateForm
    template_name = 'create-organizer.html'
    success_url = reverse_lazy('events')

class OrganizerDetailView(DetailView):
    model = Organizer
    template_name = 'details-organizer.html'
    context_object_name = 'organizer'

    def get_object(self):
        return Organizer.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Event.objects.filter(
            organizer=self.object,
            start_time__gt=timezone.now()
        ).order_by('start_time')
        return context

class OrganizerEditView(UpdateView):
    model = Organizer
    form_class = OrganizerEditForm
    template_name = 'edit-organizer.html'
    success_url = '/organizer/details/'

    def get_object(self):
        return Organizer.objects.first()

class OrganizerDeleteView(DeleteView):
    model = Organizer
    template_name = 'delete-organizer.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return Organizer.objects.first()

    def post(self, request, *args, **kwargs):
        organizer = self.get_object()

        if not organizer:
            return redirect(self.success_url)

        upcoming_events = Event.objects.filter(
            organizer=organizer,
            start_time__gt=timezone.now()
        )

        if upcoming_events.exists():
            # Added a custom error message for the user if there are upcoming events
            return self.render_to_response({
                'organizer': organizer,
                'error_message': "You can't delete your profile. There are upcoming events!"
            })

        Event.objects.filter(organizer=organizer).delete()
        organizer.delete()

        messages.success(request, "Organizer's profile and all events were deleted.")
        return redirect(self.success_url)