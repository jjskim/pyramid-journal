"""Route with names and uris associated."""


def includeme(config):
    """Include the following routes for static files and uri paths."""
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    # config.add_route('detail', '/journal/{id:\d+}') this is regex
    config.add_route('detail', '/journal/1')
    config.add_route('new', '/journal/new-entry')
    # config.add_route('detail', '/journal/{id:\d+}/edit-entry')
    config.add_route('edit', '/journal/1/edit-entry')
