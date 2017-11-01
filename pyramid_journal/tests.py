"""Test file for app views."""

from __future__ import unicode_literals
from pyramid import testing
import pytest


@pytest.fixture
def dummy_request():
    """Fixture to return a single dummy request."""
    return testing.DummyRequest()


def test_list_view_response_status_code_200(dummy_request):
    """Test that requesting list_view returns a 200 response."""
    from pyramid_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.status_code == 200


def test_detail_view_response_status_code_200(dummy_request):
    """Test that requesting detail_view returns a 200 response."""
    from pyramid_journal.views.default import detail_view
    response = detail_view(dummy_request)
    assert response.status_code == 200


def test_update_view_response_status_code_200(dummy_request):
    """Test that requesting update_view returns a 200 response."""
    from pyramid_journal.views.default import update_view
    response = update_view(dummy_request)
    assert response.status_code == 200


def test_create_view_response_status_code_200(dummy_request):
    """Test that requesting create_view returns a 200 response."""
    from pyramid_journal.views.default import create_view
    response = create_view(dummy_request)
    assert response.status_code == 200


def test_list_view_text_response_is_content_type_html(dummy_request):
    """Test that list_view returns proper content within text."""
    from pyramid_journal.views.default import list_view
    response = list_view(dummy_request)
    assert response.content_type == "text/html"


def test_list_view_text_response_has_proper_content(dummy_request):
    """Test that list_view returns proper content within text."""
    from pyramid_journal.views.default import list_view
    response = list_view(dummy_request)
    the_tag = '<div class="entry_summary">'
    assert the_tag in response.ubody


def test_detail_view_text_response_has_proper_content(dummy_request):
    """Test that detail_view returns proper content within text."""
    from pyramid_journal.views.default import detail_view
    response = detail_view(dummy_request)
    the_tag = '<a href="/journal/1/edit-entry">Edit</a>'
    assert the_tag in response.ubody


def test_edit_view_text_response_has_proper_content(dummy_request):
    """Test that edit_view returns proper content within text."""
    from pyramid_journal.views.default import update_view
    response = update_view(dummy_request)
    the_tag = '<button type="submit">Edit Post</button>'
    assert the_tag in response.ubody


def test_create_view_text_response_has_proper_content(dummy_request):
    """Test that create_view returns proper content within text."""
    from pyramid_journal.views.default import create_view
    response = create_view(dummy_request)
    the_tag = '<button type="submit">Create New</button>'
    assert the_tag in response.ubody
