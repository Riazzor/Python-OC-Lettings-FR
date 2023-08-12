import pytest
from django.http import Http404
from mixer.backend.django import mixer
from lettings.views import index, letting
from pytest_django import asserts


@pytest.fixture
def letting_data(db):
    return mixer.cycle(5).blend('lettings.Letting')


def test_index_view(rf, letting_data):
    request = rf.get('/')
    response = index(request)

    assert response.status_code == 200
    for let in letting_data:
        asserts.assertContains(response, let)


def test_letting_view(rf, letting_data):
    let = letting_data[0]

    request = rf.get(f'/lettings/{let.id}/')
    response = letting(request, let.id)

    assert response.status_code == 200
    asserts.assertContains(response, let.address)
    asserts.assertContains(response, let.title)


def test_letting_view_not_found(rf, letting_data):
    # Ensure the view raises Http404 for non-existent letting
    request = rf.get('/lettings/12345/')
    with pytest.raises(Http404):
        letting(request, 12345)
