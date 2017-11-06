"""View routes."""

from pyramid.view import view_config
from .default import home_view, detail_view, create_view, update_view


# def includeme(config):
#     """Add views to configurator and provide route names."""
#     config.add_view(list_view, route_name="home")
#     config.add_view(detail_view, route_name="detail")
#     config.add_view(create_view, route_name="new")
#     config.add_view(update_view, route_name="edit")


@view_config(route_name="home", renderer="")
def home_view(request):
    return

@view_config(route_name="detail", renderer="")
def detail_view(request):
    return

@view_config(route_name="new", renderer="")
def new_view(request):
    return

@view_config(route_name="edit", renderer="")
def edit_view(request):
    return