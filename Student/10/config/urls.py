from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/<str:doc>', DocumentView.as_view()),
]