"""madleak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path

# Importing views
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', admin.site.urls, name='admin'),
]

if settings.DEBUG:  # Don't do this in production mode

    # Importing the static function from the django.conf.urls.static module.
    from django.conf.urls.static import static

    # Adding the static files to the urlpatterns.
    urlpatterns.extend(
        static(
            settings.STATIC_URL,
            document_root=settings.STATIC_ROOT
        )
    )
