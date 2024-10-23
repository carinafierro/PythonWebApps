from django.urls import path
from hero.views import SuperheroListView, SuperheroView

urlpatterns = [
    path('<str:name>', SuperheroView.as_view()),
    path('', SuperheroListView.as_view()),
]
