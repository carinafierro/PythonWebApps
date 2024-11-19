from django.urls import include, path
from django.views.generic import SignUpView

urlpatterns = [
    # Login/Logout code
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns = [
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
]