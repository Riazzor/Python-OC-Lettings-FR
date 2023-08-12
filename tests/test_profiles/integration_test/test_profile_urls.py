import pytest
from django.urls import reverse, resolve
from pytest_django import asserts
from django.contrib.auth import get_user_model
from profiles import models, views

User = get_user_model()


@pytest.fixture
def profile(db):
    user = User.objects.create_user(username='testuser', password='testpassword')
    return models.Profile.objects.create(user=user, favorite_city='Favorite City')


@pytest.mark.django_db
def test_index_urls(client):
    index_url = reverse('profiles:index')
    resolved_url = resolve(index_url)
    assert resolved_url.func == views.index
    assert resolved_url.namespace == 'profiles'
    assert resolved_url.app_names == ['profiles']
    assert resolved_url.url_name == 'index'
    response = client.get(index_url)
    asserts.assertTemplateUsed(response, "profiles/index.html")


@pytest.mark.django_db
def test_profile_urls(profile, client):
    profile_name = profile.user.username
    profile_url = reverse('profiles:profile', args=[profile_name])
    resolved_url = resolve(profile_url)
    assert profile_url == f'/profiles/{profile_name}/'
    assert resolved_url.func == views.profile
    assert resolved_url.namespace == 'profiles'
    assert resolved_url.app_names == ['profiles']
    assert resolved_url.url_name == 'profile'
    response = client.get(profile_url)
    asserts.assertTemplateUsed(response, 'profiles/profile.html')
