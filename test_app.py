import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_exam_title_and_devops(client):
    response = client.get("/")
    html = response.data.decode("utf-8")

    # El título principal del examen debe aparecer
    assert "Entorno del Examen de DevOps" in html
    # Debe mencionar explícitamente que es el último parcial
    assert "examen del último parcial de DevOps" in html


def test_home_contains_exam_button_label(client):
    response = client.get("/")
    html = response.data.decode("utf-8")

    # El botón para probar el entorno del examen debe estar presente
    assert "Probar entorno del examen" in html
