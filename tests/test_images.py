import pytest

from Image_Repository.db import get_db


def test_index(client, auth):
    response = client.get("/images")
    assert b"image" in response.data

def test_display(client, auth):
    response = client.get("/images/display")
    assert b"Images" in response.data


@pytest.mark.parametrize("path", ("/images/delete",))
def test_login_required(client, path):
    response = client.post(path)
    assert response.headers["Location"] == "http://localhost/auth/login"


def test_upload(client, auth, app):
    auth.login()
    # assert client.post("/images/upload").status_code == 200
    client.post("/images/upload", data={"title": "created", "body": ""})

    with app.app_context():
        db = get_db()
        count = db.execute("SELECT COUNT(id) FROM images").fetchone()[0]
        assert count == 3


def test_delete(client, auth, app):
    auth.login()
    response = client.post("/images/delete")
    assert response.headers["Location"] == "http://localhost/images/display"

    with app.app_context():
        db = get_db()
        post = db.execute("SELECT * FROM images WHERE author_id = -1").fetchone()
        assert post is None
