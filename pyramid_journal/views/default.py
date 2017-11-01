"""Module with view functions that serve each uri."""


from pyramid.response import Response
import os

HERE = os.path.abspath(__file__)
TEMPLATES = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'templates')
DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


def list_view(request):
    """View for the home page."""
    with open(os.path.join(TEMPLATES, 'index.html')) as file:
        return Response(file.read())


def detail_view(request):
    """View for the detail page."""
    with open(os.path.join(DATA, 'mon_oct_30.html')) as file:
        return Response(file.read())


def create_view(request):
    """View for the create new entry page."""
    with open(os.path.join(TEMPLATES, 'new.html')) as file:
        return Response(file.read())


def update_view(request):
    """View for the edit page."""
    with open(os.path.join(TEMPLATES, 'edit.html')) as file:
        return Response(file.read())
