import pytest
import json
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
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data


def test_reset_stats(client):
    client.post("/game/stats/reset")
    res = client.get("/game/stats/")
    expected = {
        "won": 0,
        "lost": 0,
        "ratio_won": None,
    }
    data = json.loads(res.data)
    assert data == expected
    assert res.status_code == 200

