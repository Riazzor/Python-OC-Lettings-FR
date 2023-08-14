"""
Lettings App - Views

This module contains view functions for property lettings in the 'lettings' app.

View Functions:
    index(request): Renders the index page with a list of all lettings.
    letting(request, letting_id): Renders the details page for a specific letting.
"""
from django.shortcuts import render
from django.http import Http404
from lettings.models import Letting
from logger import get_logger

logger = get_logger(__name__)


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit. Sed non placerat
# massa. Integer est nunc, pulvinar a tempor et, bibendum id arcu. Vestibulum ante ipsum primis
# in faucibus orci luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Render the index page with a list of all lettings.

    This view function retrieves a list of all lettings from the database
    and renders the index page, displaying a summary of each letting.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML for the index page.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# C ras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan porta nisl id
# eleifend. Praesent dignissim, odio eu consequat pretium, purus urna vulputate arcu, vitae
# efficitur lacus justo nec purus. Aenean finibus faucibus lectus at porta. Maecenas auctor,
# est ut luctus congue, dui enim mattis enim, ac condimentum velit libero in magna. Suspendisse
# potenti. In tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum. Ut
# quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique mauris eu velit
# fermentum, tempus pharetra est luctus. Vivamus consequat aliquam libero, eget bibendum lorem.
# Sed non dolor risus. mauris condimentum auctor elementum. Donec quis nisi ligula. Integer
# vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Render the details page for a specific letting.

    This view function retrieves the letting associated with the given ID from the database
    and renders the details page, displaying detailed information about the letting.

    Args:
        request (HttpRequest): The HTTP request object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered HTML for the letting details page.
    """
    letting = Letting.objects.filter(id=letting_id)
    if not letting.exists():
        logger.warning(f'This letting object doesn\'t exists : {letting_id}')
        raise Http404()

    letting = letting.first()
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
