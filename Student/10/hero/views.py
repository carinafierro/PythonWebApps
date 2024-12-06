from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        title = "Gettysburg"
        body = 'Four score and seven years ago ...'
        return dict(title=title, body=body, color='bg-primary', width='col')
    
class CardsView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())
    
class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        document = self.kwargs.get('doc')
        path = Path('Documents')/document
        markdown_text = markdown(path.read_text())
        return dict(text=markdown_text)