import pytest
from ..hangman import app


@pytest.fixture
def client():
    # db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as cli:
        #with app.app.test_context():
        #     app.init_db()
        yield cli

    # os.close(db_fd)
    # os.unlink(app.app.config["DATABASE"])


def test_home(client):
    rv = client.get("/")
    assert b"Welcome" in rv.data
