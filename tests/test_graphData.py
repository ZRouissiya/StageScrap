from app import app

def test_graphData():
    client=app.test_client()
    url='/graph-data-domaine'
    response=client.get(url)
    assert response.status_code==200