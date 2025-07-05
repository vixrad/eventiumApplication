from django.views.generic import TemplateView
from common.mixins import OrganizerProfileMixin

class IndexView(OrganizerProfileMixin, TemplateView):
    template_name = 'index.html'