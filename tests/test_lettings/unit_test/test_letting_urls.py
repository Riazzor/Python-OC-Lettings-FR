import pytest
from django.urls import reverse, resolve
from pytest_django import asserts

from lettings import models, views


@pytest.fixture
def letting(db):
    address = models.Address.objects.create(
        number=123,
        street='Letting street',
        city='Let City',
        state='State Let',
        zip_code=118,
        country_iso_code='Ltt',
    )
    return models.Letting.objects.create(title='The Letting', address=address)


@pytest.mark.django_db
def test_index_urls(client):
    index_url = reverse('lettings:index')
    resolved_url = resolve(index_url)
    assert resolved_url.func == views.index
    assert resolved_url.namespace == 'lettings'
    assert resolved_url.app_names == ['lettings']
    assert resolved_url.url_name == 'index'
    response = client.get(index_url)
    asserts.assertTemplateUsed(response, "lettings/index.html")


@pytest.mark.django_db
def test_letting_urls(letting, client):
    letting_id = letting.id
    letting_url = reverse('lettings:letting', args=[letting_id])
    resolved_url = resolve(letting_url)
    assert letting_url == f'/lettings/{letting_id}/'
    assert resolved_url.func == views.letting
    assert resolved_url.namespace == 'lettings'
    assert resolved_url.app_names == ['lettings']
    assert resolved_url.url_name == 'letting'
    response = client.get(letting_url)
    asserts.assertTemplateUsed(response, 'lettings/letting.html')
    # assert False
