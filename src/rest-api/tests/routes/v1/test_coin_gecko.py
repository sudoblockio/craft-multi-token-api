from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_pairs(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/pairs")
    response = r.json()
    assert r.status_code == 200
    assert response

def test_get_tickers(prep_recent_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/tickers")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert len(response) > 0

    assert response[0]["last_price"] == 9
    assert response[0]["base_volume"] == 9
    assert response[0]["target_volume"] == 18
    assert response[0]["high"] == 9
    assert response[0]["low"] == 1

def test_get_historical_no_timestamps(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/historical_trades?ticker_id=sICX_ICX")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert response["buy"]
    assert len(response["buy"]) == 4

    assert response["sell"]
    assert len(response["sell"]) == 5


def test_get_historical_start_timestamp(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/historical_trades?ticker_id=sICX_ICX&start_time=900000")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert response["buy"]
    assert len(response["buy"]) == 3

    assert response["sell"]
    assert len(response["sell"]) == 3


def test_get_historical_end_timestamp(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/historical_trades?ticker_id=sICX_ICX&end_time=900000")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert response["buy"]
    assert len(response["buy"]) == 1

    assert response["sell"]
    assert len(response["sell"]) == 2


def test_get_historical_both_timestamps(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/coin-gecko/historical_trades?ticker_id=sICX_ICX&start_time=900000&end_time=2600000")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert response["buy"]
    assert len(response["buy"]) == 2

    assert response["sell"]
    assert len(response["sell"]) == 1

