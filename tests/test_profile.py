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

def test_profile_success(client):
    client=app.test_client()
    url='/profile'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)

    response=client.get(url)
    assert response.status_code == 200

def test_profile_not_authentificated(client):
    client=app.test_client()
    url='/profile'
    with client.session_transaction() as sess:
            sess['user'] = ""
    response=client.get(url)
    assert response.status_code == 303

def test_profile_unauthorized(client):
    client=app.test_client()
    url='/profile'
    response=client.get(url)
    assert response.status_code == 401

def test_changePassword_success(client):
    client=app.test_client()
    url='/changePassword'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.post(url,data={'current_password':'123','new_password':'123'})
    assert response.status_code == 200

def test_changePassword_fail(client):
    client=app.test_client()
    url='/changePassword'
    user=User('Zouhair','Rouissiya','test@123.fr','123',userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.post(url,data={'current_password':'','new_password':'123'})
    assert response.status_code == 301

def test_changePassword_not_authentificated(mocker,client):
    client=app.test_client()
    url='/changePassword'
    user=User(name='Zouhair',lastName='Rouissiya',email='test@123.fr',password="123",userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    mocker.patch.object(User, 'updatePassword', side_effect=Exception("Error"))
    response=client.post(url,data={'current_password':'123','new_password':'123'})
    assert response.status_code == 302

def test_changePassword_fail(client):
    client=app.test_client()
    url='/changePassword'
    response=client.post(url,data={'current_password':'123','new_password':'123'})
    assert response.status_code == 500

def test_updateData_success(client):
    client=app.test_client()
    url='/updateData'
    user=User(name='Zouhair',lastName='Rouissiya',email='test@123.fr',password="123",userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.post(url,data={'nom':'test','prenom':'test','email':'test@123.fr'})
    assert response.status_code==200

def test_updateData_email_fail(client):
    client=app.test_client()
    url='/updateData'
    user=User(name='Zouhair',lastName='Rouissiya',email='test@123.fr',password="123",userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.post(url,data={'nom':'Rouissiya','prenom':'Zouhair','email':'rouissiya@gmail.com'})
    assert response.status_code==301

def test_updateData_fail(client):
    client=app.test_client()
    url='/updateData'
    user=User(name='Zouhair',lastName='Rouissiya',email='test@123.fr',password="123",userId=22)
    with client.session_transaction() as sess:
            sess['user'] = pickle.dumps(user)
    response=client.post(url,data={'nom':'','prenom':'','email':'test@123.fr'})
    assert response.status_code==302
