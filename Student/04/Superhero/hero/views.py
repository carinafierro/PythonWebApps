from django.views.generic import TemplateView

class SuperheroView(TemplateView):
    template_name = 'index.html'

