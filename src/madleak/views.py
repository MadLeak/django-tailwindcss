""" Imports """
from django.shortcuts import render


def home_view(request):
    """ Render home view """
    return render(request, 'pages/home.html', {})
