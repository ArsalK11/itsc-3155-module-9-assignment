# TODO: Feature 1
from app import app

client = app.test_client()

def test_list_all_movies():
    response = client.get('/')
    assert response.status_code == 200
    assert b'All Movies' in response.data
