from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from events.forms import EventForm
from events.models import Event
from organizers.models import Organizer


class EventsListView(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'
    ordering = ['-start_time']

class EventCreateView(CreateView):
    model = Event
    template_name = 'create-event.html'
    context_object_name = 'event'
    form_class = EventForm
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        organizer = Organizer.objects.first()
        form.instance.organizer = organizer
        return super().form_valid(form)

class EventDetailView(DetailView):
    model = Event
    template_name = 'details-event.html'
    context_object_name = 'event'


class EventEditView(UpdateView):
    model = Event
    template_name = 'edit-event.html'
    context_object_name = 'event'
    form_class = EventForm

    def form_valid(self, form):
        form.instance.organizer = self.object.organizer or Organizer.objects.first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('event-details', kwargs={'pk': self.object.pk})

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'delete-event.html'
    context_object_name = 'event'
    success_url = reverse_lazy('events')