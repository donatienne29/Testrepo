# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    # Configure Flask pour le mode test
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test de la route d'accueil."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, this is my Flask app!"

def test_data(client):
    """Test de la route API /api/data."""
    response = client.get('/api/data')
    assert response.status_code == 200
    assert response.get_json() == {"message": "This is sample data"}
