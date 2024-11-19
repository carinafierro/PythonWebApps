from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
]

from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]