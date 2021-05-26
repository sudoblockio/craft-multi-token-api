from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_transactions(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/loans/transactions")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/transactions?limit=3")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 3


def test_get_transactions_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/loans/transactions/withdrawCollateral")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/transactions/withdrawCollateral?limit=4")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/transactions/updateStanding")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/transactions/updateStanding?limit=2")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 2


def test_get_logs(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/loans/logs")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/logs?limit=4")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 4


def test_get_logs_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/loans/logs/LoanRepaid")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/logs/LoanRepaid?limit=5")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/logs/OriginateLoan")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/loans/logs/OriginateLoan?limit=2")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 2


def test_get_loans_by_address(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/loans/hx95bb62ce10924bc26b2ff982df855fdb8c89bb56")
    response = r.json()
    assert r.status_code == 200
    assert response

