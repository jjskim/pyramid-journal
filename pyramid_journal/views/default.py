"""Module with view functions that serve each uri."""


from ..data import journal_list
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config


@view_config(route_name='list_view', renderer='../templates/index.jinja2')
def list_view(request):
    """View config for list view."""
    return {
        "journals": journal_list.JOURNALS
    }


@view_config(route_name='detail_view', renderer='../templates/detail.jinja2')
def detail_view(request):
    """View config for detail view."""
    journal_id = int(request.matchdict['id'])
    if journal_id < 0 or journal_id > len(journal_list.JOURNALS):
        raise HTTPNotFound
    the_journal = list(filter(lambda x: x['id'] == journal_id, journal_list.JOURNALS))[0]
    return {
        'journal': the_journal
    }


@view_config(route_name='update_view', renderer='../templates/edit.jinja2')
def update_view(request):
    """View config for update view."""
    journal_id = int(request.matchdict['id'])
    if journal_id < 0 or journal_id > len(journal_list.JOURNALS):
        raise HTTPNotFound
    the_journal = list(filter(lambda x: x['id'] == journal_id, journal_list.JOURNALS))[0]
    return {
        'journal': the_journal
    }


@view_config(route_name='create_view', renderer='../templates/new.jinja2')
def create_view(request):
    """View config for create view."""
    return {}
