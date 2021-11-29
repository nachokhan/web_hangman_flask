import pytest
import json
from ..hangman import app


@pytest.fixture
def client():
    # db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.config["TESTING"] = True

    with app.test_client() as cli:
        # with app.app.test_context():
        #     app.init_db()
        yield cli

    # os.close(db_fd)
    # os.unlink(app.app.config["DATABASE"])


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome" in res.data


def test_reset_stats_return_correct_dict(client):
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


def test_new_game_has_word_length(client):
    res = client.post("/game/new")

    data = json.loads(res.data)

    assert "status" in data
    assert "word_length" in data['status']
    assert data['status']['word_length'] > 0


def test_new_game_returns_correct_dict(client):
    res = client.post("/game/new")

    data = json.loads(res.data)

    # pick the data as I don't know -yet- how to mock it
    aux_word_length = data['status']['word_length']

    expected = {
        "status": {
            "incorrect_guesses": 0,
            "game_state": "in_progress",
            "word_length": aux_word_length,
            "guesses": {},
        }
    }

    assert data == expected
    assert res.status_code == 200


@pytest.fixture
def client_for_loose():
    app.config["TESTING"] = True

    with app.test_client() as cli:
        with cli.session_transaction() as sess:
            sess['lost_games'] = 0
            sess['won_games'] = 0
            sess['incorrect_guesses'] = 9
            sess['game_state'] = 'in_progress'
            sess['word_length'] = 6
            sess['word'] = "cactus"
            sess['guesses'] = {}
            sess['correct_letters'] = []
            sess['incorrect_letters'] = [
                'q', 'w', 'v', 'e', 'o', 'p', 'b', 'n', 'm'
            ]
            sess['remaining_letters'] = len(sess['word'])
        yield cli


def test_check_letter(client_for_loose):
    res = client_for_loose.post("/game/check-letter/c")

    data = json.loads(res.data)

    expected = {
        "status": {
            "incorrect_guesses": 9,
            "game_state": "in_progress",
            "word_length": 6,
            "guesses": {
                "c": [0, 2],
            },
        },
        "error": None,
    }

    assert data == expected
    assert res.status_code == 200


def test_check_letter_lost(client_for_loose):
    res = client_for_loose.post("/game/check-letter/k")

    data = json.loads(res.data)

    expected = {
        "status": {
            "incorrect_guesses": 10,
            "game_state": "lost",
            "word_length": 6,
            "guesses": {}
        },
        "error": None,
    }

    assert data == expected
    assert res.status_code == 200


@pytest.fixture
def client_for_win():
    app.config["TESTING"] = True

    with app.test_client() as cli:
        with cli.session_transaction() as sess:
            sess['lost_games'] = 0
            sess['won_games'] = 0
            sess['incorrect_guesses'] = 9
            sess['game_state'] = 'in_progress'
            sess['word_length'] = 6
            sess['word'] = "cactus"
            sess['guesses'] = {
                'a': [1],
                't': [3],
                'u': [4],
                's': [5],
            }
            sess['correct_letters'] = [
                'a', 't', 'u', 's'
            ]
            sess['remaining_letters'] = 1
            sess['incorrect_letters'] = [
                'q', 'w', 'v', 'e', 'o', 'p', 'b', 'n', 'm'
            ]
        yield cli


def test_check_letter_win(client_for_win):
    res = client_for_win.post("/game/check-letter/c")

    data = json.loads(res.data)

    expected = {
        "status": {
            "incorrect_guesses": 9,
            "game_state": "won",
            "word_length": 6,
            "guesses": {
                'a': [1],
                't': [3],
                'u': [4],
                's': [5],
                'c': [0,2],
            }
        },
        "error": None,
    }

    assert data == expected
    assert res.status_code == 200
