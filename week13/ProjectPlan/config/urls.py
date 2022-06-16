"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [

    # Admin
    # path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='doc/Index')),

    # Project Plan
    path('accounts/', include('django.contrib.auth.urls')),
    path('developer/', include('swplan.urls_developer')),
    path('doc/', include('swplan.urls_doc')),
    path('milestone/', include('swplan.urls_milestone')),
    path('project/', include('swplan.urls_project')),

]