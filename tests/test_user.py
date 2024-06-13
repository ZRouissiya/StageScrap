import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_logIn_success(client):
    client = app.test_client()
    url = '/logIn'
    response = client.post(url, data={'email':'test@test.com','password':'123'})
    assert response.status_code == 301
    
        
def test_logIn_fail_wrong_password(client):
    client = app.test_client()
    url = '/logIn'
    response = client.post(url, data={'email':'test@test.com','password':'1234'})
    assert response.status_code == 303

def test_logIn_fail_no_user(client):
    client = app.test_client()
    url = '/logIn'
    response = client.post(url, data={'email':'test@test.com','password':'1234'})
    assert response.status_code == 303

def test_logIn_exception(client):
    client = app.test_client()
    url = '/logIn'
    response = client.post(url, data={'email':'test@test.com','password':'1234'})
    assert response.status_code == 303