import json

import pytest
from .. import crud


def test_read_post(test_app, monkeypatch):
    test_data = {"id": 1, "text": "something", "created_by": "something else"}

    async def mock_get(id):
        return test_data

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/posts/1")
    assert response.status_code == 200
    assert response.json() == test_data


def test_read_post_incorrect_id(test_app, monkeypatch):
    async def mock_get(id):
        return None

    monkeypatch.setattr(crud, "get", mock_get)

    response = test_app.get("/posts/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_read_all_posts(test_app, monkeypatch):
    test_data = [
        {"text": "something", "created_by": "something else", "id": 1},
        {"text": "someone", "created_by": "someone else", "id": 2},
    ]

    async def mock_get_all():
        return test_data

    monkeypatch.setattr(crud, "get_all", mock_get_all)

    response = test_app.get("/posts/")
    assert response.status_code == 200
    assert response.json() == test_data