from organizers.models import Organizer

class OrganizerProfileMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizer_profile'] = Organizer.objects.exists()
        return context