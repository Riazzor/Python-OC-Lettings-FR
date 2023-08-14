"""
Profiles App - Views

This module contains view functions for user profiles in the 'profiles' app.

View Functions:
    index(request): Renders the index page with a list of all profiles.
    profile(request, username): Renders the profile page for a specific user.
"""
from django.shortcuts import render
from django.http import Http404
from profiles.models import Profile
from logger import get_logger


logger = get_logger(__name__)


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis
# dictum lacus d
def index(request):
    """
    Render the index page with a list of all profiles.

    This view function retrieves a list of all profiles from the database and renders
    the index page, displaying a summary of each profile.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML for the index page.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt, dolor
# id facilisis fringilla, eros leo tristique lacus, it. Nam aliquam dignissim congue. Pellentesque
# habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Render the profile page for a specific user.

    This view function retrieves the profile associated with the given username from the database
    and renders the profile page, displaying detailed information about the user's profile.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to retrieve.

    Returns:
        HttpResponse: The rendered HTML for the profile page.
    """
    profile = Profile.objects.filter(user__username=username)
    if not profile.exists():
        logger.warning(f'This profile does\'nt exists : {username}')
        raise Http404()
    context = {'profile': profile.first()}
    return render(request, 'profiles/profile.html', context)
