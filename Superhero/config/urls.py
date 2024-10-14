from django.urls import path
from hero.views import HulkView, IronManView

urlpatterns = [
    path('',        HulkView.as_view()),
    path('',        IronManView.as_view()),
]