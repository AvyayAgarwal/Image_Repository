from Image_Repository import create_app


def test_config():
    """Test create_app without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_health(client):
    response = client.get("/health")
    assert response.data == b"Green"