from pathlib import Path 
from django.views.generic import TemplateView 

data = {
    'hero': {
        'title': 'Batman',
        'id': 'Bruce Wayne',
        'image': '/static/images/batman.jpg',
        'strengths': 'smart, knows martial arts ',
        'weaknesses': 'no superpowers, injured easily, trust issues',
    },
    'hero': {
        'name': 'Captain America',
        'id': 'Steve Rogers',
        'image': '/static/images/captain_america.jpg',
        'strengths': 'speed, endurance, smart',
        'weaknesses': 'limitations to injuries, isolated',
    },
    'hero': {
        'name': 'Superman',
        'id': 'Clark Kent',
        'image': '/static/images/superman.jpg',
        'strengths': 'super fast, heat vision, can fly',
        'weaknesses': 'kryptonite, isolated, overexertion',
    },
    'hero': {
        'name': 'Wolverine',
        'id': 'Logan',
        'image': '/static/images/wolverine.jpg',
        'strengths': 'good instincts, martial arts, good senses',
        'weaknesses': 'rage, adamantium, isolated',
    },
    'hero': {
        'name': 'Wonder Woman',
        'id': 'Diana Prince',
        'image': '/static/images/wonder_woman.jpg',
        'strengths': 'strategic thinking, fast healing, combat skills',
        'weaknesses': 'over protetive, vulnerable to magic, isolated',
    },
}
class SuperheroView(TemplateView):
    template_name = 'hero.html'

    def get_context_dat(self, **kwargs):
        return {'hero': data}
    
    def get_context_data(self, **kwargs):
        name = kwargs['name']
        image = f'/static/images/{name}'
        return {'hero': image}
    
    
    
class SuperheroListView(TemplateView):
    template_name = 'heroes.html'

    def get_context_data(self, **kwargs):
        h = Path('static/images').iterdir()
        h = [f for f in h]
        return dict(heroes=h)