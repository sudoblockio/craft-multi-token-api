from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_transactions(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/bnusd/transactions")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/bnusd/transactions?limit=6")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 3


def test_get_transactions_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/bnusd/transactions/transfer")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/bnusd/transactions/transfer?limit=6")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 3


def test_get_logs(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/bnusd/logs")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/bnusd/logs?limit=6")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 3


def test_get_logs_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/bnusd/logs/Mint")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/bnusd/logs/Burn")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/bnusd/logs/Transfer")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

