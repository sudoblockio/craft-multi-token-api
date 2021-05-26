from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_exchange_rate(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/band/exchange-rate?base=USD&quote=ICX")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert response["rate"]
    assert response["last_update_base"]
    assert response["last_update_quote"]

def test_get_exchange_rate_no_base(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/band/exchange-rate?quote=ICX")
    response = r.json()
    assert r.status_code == 422

def test_get_exchange_rate_no_quote(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/band/exchange-rate?base=USD")
    response = r.json()
    assert r.status_code == 422

def test_get_exchange_rate_no_parameters(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/band/exchange-rate")
    response = r.json()
    assert r.status_code == 422

