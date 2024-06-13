import pytest
from models.user import User
import pickle
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret_key'
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_dashboard_success(mocker,client):
    client=app.test_client()
    url='/dashboard'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.get(url)
    assert response.status_code == 200

def test_dashboard_not_authentificated(client):
    client=app.test_client()
    url='/dashboard'
    response=client.get(url)
    assert response.status_code == 302
