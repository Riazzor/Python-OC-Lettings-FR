import pytest
from lettings.models import Address, Letting


@pytest.fixture
def sample_address(db):
    return Address.objects.create(
        number=123,
        street='Sample Street',
        city='Sample City',
        state='SS',
        zip_code=12345,
        country_iso_code='XYZ'
    )


@pytest.fixture
def sample_letting(db, sample_address):
    return Letting.objects.create(
        title='Sample Letting',
        address=sample_address
    )


def test_address_str_representation(sample_address):
    assert str(sample_address) == '123 Sample Street'


def test_letting_str_representation(sample_letting):
    assert str(sample_letting) == 'Sample Letting'
