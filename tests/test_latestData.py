from app import app


def test_latestData():
    client=app.test_client()
    url='/latest-data'
    response=client.get(url)
    assert response.status_code==200