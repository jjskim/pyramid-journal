"""Module with view functions that serve each uri."""


# from pyramid.response import Response
# import os

# HERE = os.path.abspath(__file__)
# TEMPLATES = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'templates')
# DATA = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'data')


# def list_view(request):
#     """View for the home page."""
#     with open(os.path.join(TEMPLATES, 'index.html')) as file:
#         return Response(file.read())


# def detail_view(request):
#     """View for the detail page."""
#     with open(os.path.join(DATA, 'mon_oct_30.html')) as file:
#         return Response(file.read())


# def create_view(request):
#     """View for the create new entry page."""
#     with open(os.path.join(TEMPLATES, 'new.html')) as file:
#         return Response(file.read())


# def update_view(request):
#     """View for the edit page."""
#     with open(os.path.join(TEMPLATES, 'edit.html')) as file:
#         return Response(file.read())

from pyramid.view import view_config
from pyramid_journal.data.data import ENTRIES

import os

HERE = os.path.dirname(__file__)


@view_config(route_name='home', renderer="../templates/list_view.jinja2")
def list_view(request):
    """View config for list view."""
    return {"entries": ENTRIES}


@view_config(route_name="detail", renderer="../templates/detail_view.jinja2")
def detail_view(request):
    """View config for detail view."""
    the_id = int(request.matchdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            return {"entry": entry}


@view_config(route_name="create", renderer="../templates/create_view.jinja2")
def create_view(request):
    """View config for create view."""
    return {}


@view_config(route_name="update", renderer="../templates/update_view.jinja2")
def update_view(request):
    """View config for update view."""
    the_id = int(request.matcdict['id'])
    for entry in ENTRIES:
        if entry['id'] == the_id:
            return {"entry": entry}
