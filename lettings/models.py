"""
Models for Address and Letting in the OC Lettings Site.

This module defines the database models for representing property addresses
and lettings in the OC Lettings Site.

Models:
    Address: Represents a property address with street information, city, state, zip code,
        and country ISO code.
    Letting: Represents a letting with a title and a one-to-one relationship to an Address.
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Model representing a property address.

    Attributes:
        number (PositiveIntegerField): The property number in the address (max value: 9999).
        street (CharField): The street name of the address (max length: 64).
        city (CharField): The city name of the address (max length: 64).
        state (CharField): The state abbreviation of the address (max length: 2).
        zip_code (PositiveIntegerField): The ZIP code of the address (max value: 99999).
        country_iso_code (CharField): The ISO country code of the address (max length: 3).

    Methods:
        __str__(): Return a human-readable representation of the address.
    """
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """
        Return a human-readable representation of the address.

        Returns:
            str: The formatted address string.
        """
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a human-readable representation of the letting.

        Returns:
            str: The title of the letting.
        """
        return self.title
