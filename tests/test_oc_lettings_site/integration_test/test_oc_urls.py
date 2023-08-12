from django.urls import reverse, resolve
from pytest_django import asserts

from oc_lettings_site import views


def test_index_urls(client):
    index_url = reverse('index')
    resolved_url = resolve(index_url)
    assert resolved_url.func == views.index
    assert resolved_url.url_name == 'index'
    response = client.get(index_url)
    asserts.assertTemplateUsed(response, "oc_lettings_site/index.html")
