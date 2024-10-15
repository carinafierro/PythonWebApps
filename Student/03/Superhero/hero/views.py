from django.views.generic import TemplateView

class BatmanView(TemplateView):
    template_name = 'hero1.html'

def get_context_data(self, **kwargs):
        return {
            'title': 'Batman',
            'id': 'Bruce Wayne',
            'image': '/static/images/batman.jpg'
        }

class WonderWomanView(TemplateView):
    template_name = 'hero2.html'
    
def get_context_data(self, **kwargs):
        return {
            'title': 'Wonder Woman',
            'id': 'Diana Prince',
            'image': '/static/images/wonder_woman.jpg'
        }

class SupermanView(TemplateView):
    template_name = 'hero3.html'
    
def get_context_data(self, **kwargs):
        return {
            'title': 'Superman',
            'id': 'Clark Kent',
            'image': '/static/images/superman.jpg'
        }

class HeroListView(TemplateView):
    template_name = 'heroes.html'
    
def get_context_data(self, **kwargs):
        return {
            'title': 'Superman',
            'id': 'Clark Kent',
            'image': '/static/images/superman.jpg'
        }