from oc_lettings_site import views


def test_index_view(rf):
    request = rf.get('/')
    response = views.index(request)
    assert response.status_code == 200
    assert b'Welcome to Holiday Homes' in response.content
