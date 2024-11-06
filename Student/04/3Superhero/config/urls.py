from django.urls import path
from django.contrib.admin import site
from hero.views import SuperheroListView, SuperheroView

urlpatterns = [
    path('<str:name>', SuperheroView.as_view()),
    path('', SuperheroListView.as_view()),
]
