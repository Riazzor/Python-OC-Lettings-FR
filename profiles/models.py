"""
Profiles App - Profile Model

This module defines the 'Profile' model for user profiles in the 'profiles' app.

Model:
    Profile: Represents user profiles with a one-to-one relationship to the User model.

Attributes:
    user (OneToOneField): A one-to-one relationship with the User model.
    favorite_city (CharField): The user's favorite city (max length: 64, can be blank).

Methods:
    __str__(): Return a human-readable representation of the profile.
"""
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    """
    Represents user profiles with a one-to-one relationship to the User model.

    Attributes:
        user (OneToOneField): A one-to-one relationship with the User model.
        favorite_city (CharField): The user's favorite city (max length: 64, can be blank).
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Return a human-readable representation of the profile.

        Returns:
            str: The username of the associated user.
        """
        return self.user.username
