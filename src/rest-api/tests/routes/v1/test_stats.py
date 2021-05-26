from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_borrowers(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/num_borrowers")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert response["num_borrowers"]


def test_get_total_transactions(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/total-transactions")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert response["total_transactions"] == 7
    assert response["dex_transactions"] == 3
    assert response["loans_transactions"] == 4


def test_get_total_value_locked(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/total-value-locked")
    response = r.json()
    assert r.status_code == 200
    assert response
    # assert response["total_value_locked_icx"]
    assert response["dex_value_locked_icx"]
    assert response["loans_value_locked_sicx"]
    assert response["sicx_icx_ratio"]


def test_get_stats_loans_chart(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/loans-chart?start_timestamp=1&end_timestamp=20&time_interval=5")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert len(response) == 4

    assert response[0]["value"] == "0x1"
    assert response[0]["time"] == 1

    assert response[1]["value"] == "0x4"
    assert response[1]["time"] == 6

    assert response[2]["value"] == "0x7"
    assert response[2]["time"] == 11

    assert response[3]["value"] == "0xc"
    assert response[3]["time"] == 16


def test_get_stats_loans_chart_start_later(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/loans-chart?start_timestamp=11&end_timestamp=20&time_interval=5")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert len(response) == 2

    assert response[0]["value"] == "0x7"
    assert response[0]["time"] == 11

    assert response[1]["value"] == "0xc"
    assert response[1]["time"] == 16


def test_get_stats_collateral_chart(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/collateral-chart?start_timestamp=1&end_timestamp=20&time_interval=5")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert len(response) == 4

    assert response[0]["value"] == "0x1"
    assert response[0]["time"] == 1

    assert response[1]["value"] == "0x4"
    assert response[1]["time"] == 6

    assert response[2]["value"] == "0x7"
    assert response[2]["time"] == 11

    assert response[3]["value"] == "0xc"
    assert response[3]["time"] == 16


def test_get_stats_collateral_chart_start_later(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/stats/collateral-chart?start_timestamp=11&end_timestamp=20&time_interval=5")
    response = r.json()
    assert r.status_code == 200
    assert response

    assert len(response) == 2

    assert response[0]["value"] == "0x7"
    assert response[0]["time"] == 11

    assert response[1]["value"] == "0xc"
    assert response[1]["time"] == 16

