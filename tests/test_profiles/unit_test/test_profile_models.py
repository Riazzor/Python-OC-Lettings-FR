import pytest
from profiles.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def sample_user(db):
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def sample_profile(db, sample_user):
    return Profile.objects.create(user=sample_user, favorite_city='Test City')


def test_profile_str_representation(sample_profile):
    assert str(sample_profile) == 'testuser'
