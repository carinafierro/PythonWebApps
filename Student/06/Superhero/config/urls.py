from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
