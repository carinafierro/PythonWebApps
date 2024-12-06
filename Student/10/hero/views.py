from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        title = "Gettysburg"
        body = 'Four score and seven years ago ...'
        return dict(title=title, body=body, color='bg-primary', width='col')