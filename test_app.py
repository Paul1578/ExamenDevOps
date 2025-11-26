import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as client:
        yield client


def test_index_returns_200_and_message(client):
    response = client.get("/")
    assert response.status_code == 200

    data = response.get_json()
    assert data is not None
    assert data.get("message") == "Hello, World, esto es para el examen de DevOps!"


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200

    data = response.get_json()
    assert data is not None
    assert data.get("status") == "ok"
