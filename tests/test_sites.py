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

def test_stagiaire_success(client):
    client=app.test_client()
    url='/stagiaire'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
            sess['stagiaires']=[{'Date de debut':'123', 'Niveau':'123', 'Ecole':'123', 'Secteur':'123', 'Lieu':'123','Lien':'123'}]
            sess['fields']=['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']

    response=client.get(url)
    assert response.status_code == 200

def test_stagiaire_pages_success(client):
    client=app.test_client()
    url='/stagiaire/2'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
            sess['fields']=['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']

    response=client.get(url)
    assert response.status_code == 200

def test_stagiaire_pages_unauthorized(client):
    client=app.test_client()
    url='/stagiaire/2'
    response=client.get(url)
    assert response.status_code == 401

def test_stagiaire_unauthorized(client):
    client=app.test_client()
    url='/stagiaire'
    response=client.get(url)
    assert response.status_code == 401


