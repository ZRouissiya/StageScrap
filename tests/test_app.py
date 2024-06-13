from app import app

def test_base_route():
    client=app.test_client()
    url='/'
    response=client.get(url)
    assert response.status_code==200