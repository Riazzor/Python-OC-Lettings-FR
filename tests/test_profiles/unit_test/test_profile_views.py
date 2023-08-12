import pytest
from django.http import Http404
from mixer.backend.django import mixer
from profiles.views import index, profile
from pytest_django import asserts


@pytest.fixture
def profile_data(db):
    # Create sample Profile instances for testing
    return mixer.cycle(5).blend('profiles.Profile')


def test_index_view(profile_data, rf):
    request = rf.get('/profiles/')
    response = index(request)
    assert response.status_code == 200
    for pf in profile_data:
        asserts.assertContains(response, pf)


def test_profile_view(profile_data, rf):
    username = profile_data[0].user.username
    request = rf.get(f'/profiles/{username}/')
    response = profile(request, username)
    assert response.status_code == 200
    asserts.assertContains(response, username)


def test_profile_view_not_found(rf, profile_data):
    request = rf.get('profiles/auie/')
    with pytest.raises(Http404):
        profile(request, 'auie')
