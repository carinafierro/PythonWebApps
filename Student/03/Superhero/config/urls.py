from django.urls import path
from hero.views import BatmanView, WonderWomanView, SupermanView

urlpatterns = [
    path('batman',        BatmanView.as_view()),
    path('wonderwoman',        WonderWomanView.as_view()),
    path('superman',        SupermanView.as_view()),
]