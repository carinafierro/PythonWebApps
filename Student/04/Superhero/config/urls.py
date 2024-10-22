from django.urls import path
from hero.views import SuperheroView

urlpatterns = [
    path('', SuperheroView.as_view()),
]
