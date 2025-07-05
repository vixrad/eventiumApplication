from organizers.models import Organizer

def organizer_profile(request):
    return {
        'organizer_profile': Organizer.objects.first()
    }