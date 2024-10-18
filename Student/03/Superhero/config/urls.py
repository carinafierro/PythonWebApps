from django.urls import path
from hero.views import HeroDetailView, HeroListView

urlpatterns = [
    path('batman',        HeroDetailView.as_view()),
    path('wonderwoman',        HeroDetailView.as_view()),
    path('superman',        HeroDetailView.as_view()),
]