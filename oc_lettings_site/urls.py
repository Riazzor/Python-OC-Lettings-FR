from django.contrib import admin
from django.urls import include, path

from oc_lettings_site import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('lettings/', views.lettings_index, name='lettings_index'),
    # path('lettings/<int:letting_id>/', views.letting, name='letting'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
