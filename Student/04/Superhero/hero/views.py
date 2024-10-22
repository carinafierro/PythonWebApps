from typing import Any
from django.views.generic import TemplateView

class SuperheroView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {'hero': "static\images\captain_america.jpg"}