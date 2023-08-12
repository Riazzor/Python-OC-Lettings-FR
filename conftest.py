import pytest
from django.test import Client, RequestFactory


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def client():
    return Client()
