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

def test_downloadXlsxStagiaire_success(client):
    client=app.test_client()
    url='/downloadXlsx/stagiaires'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
            sess['stagiaires']=[{'Date de debut':'123', 'Niveau':'123', 'Ecole':'123', 'Secteur':'123', 'Lieu':'123','Lien':'123'}]
            sess['fields']=['Date de debut', 'Niveau', 'Ecole', 'Secteur', 'Lieu','Lien']
    response=client.get(url)
    assert response.status_code==200

def test_downloadXlsxStagiaire_fail(client):
    client=app.test_client()
    url='/downloadXlsx/stagiaires'   
    response=client.get(url)
    assert response.status_code==500

def test_downloadXlsxMA_success(client):
    client=app.test_client()
    url='/downloadXlsx/marocAnnonces'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
            sess['marocAnnonces']=[{'Titre':'123', 'Domaine':'123', 'Duree':'123', 'Niveau':'123', 'Lien':'123'}]
            sess['fields']=['Titre', 'Domaine', 'Duree', 'Niveau', 'Lien']
    response=client.get(url)
    assert response.status_code==200

def test_downloadXlsxMA_fail(client):
    client=app.test_client()
    url='/downloadXlsx/marocAnnonces'   
    response=client.get(url)
    assert response.status_code==500