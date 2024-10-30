from pathlib import Path 
from django.views.generic import TemplateView 

class SuperheroView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f'/static/images/{name}'
        return {'hero': image}
    
    
class SuperheroListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        h = Path('static/images').iterdir()
        h = [f for f in h]
        return dict(heroes=h)