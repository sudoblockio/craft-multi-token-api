from fastapi.testclient import TestClient

from app.core.config import settings


def test_get_transactions(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/transactions")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/transactions?limit=6")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 6


def test_get_transactions_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/transactions/add")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/transactions/add?limit=4")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 4

    r = client.get(f"{settings.PREFIX}/dex/transactions/remove")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/transactions/remove?limit=2")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 2


def test_get_logs(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/logs")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/logs?limit=3")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 3


def test_get_logs_by_method(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/logs/TransferSingle")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/logs/TransferSingle?limit=1")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/logs/Swap")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1

    r = client.get(f"{settings.PREFIX}/dex/logs/Swap?limit=1")
    response = r.json()
    assert r.status_code == 200
    assert response
    assert len(response) == 1


def test_get_stats(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/stats/1")
    response = r.json()
    assert r.status_code == 200
    assert response


def test_get_stats_invalid_market_id(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/stats/bad-market-id")
    response = r.json()
    assert r.status_code == 400 # Bad request
    assert response


def test_get_balance_of(prep_fixtures, client: TestClient) -> None:
    # Fine to leave request as constant since the blockchain is immutable
    r = client.get(f"{settings.PREFIX}/dex/balance-of/hxe7af5fcfd8dfc67530a01a0e403882687528dfcb/2")
    response = r.json()
    assert r.status_code == 200
    assert response


def test_get_balance_of_invalid_address(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/balance-of/0xbadaddress/2")
    response = r.json()
    assert r.status_code == 400 # Bad request
    assert response


def test_get_swap_chart_5m(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/swap-chart/0/5m/0/1000000000")
    response = r.json()
    assert r.status_code == 200
    assert len(response) == 4

    assert response[0][0] == 0  # Timestamp
    assert response[0][1] == 1  # Open
    assert response[0][2] == 3  # Close
    assert response[0][3] == 3  # High
    assert response[0][4] == 1  # Low
    assert response[0][5] == 3  # Volume

    assert response[1][0] == 300000000
    assert response[1][1] == 3
    assert response[1][2] == 6
    assert response[1][3] == 6
    assert response[1][4] == 3
    assert response[1][5] == 3

    assert response[2][0] == 600000000
    assert response[2][1] == 6
    assert response[2][2] == 6
    assert response[2][3] == 6
    assert response[2][4] == 6
    assert response[2][5] == 0

    assert response[3][0] == 900000000
    assert response[3][1] == 6
    assert response[3][2] == 9
    assert response[3][3] == 9
    assert response[3][4] == 6
    assert response[3][5] == 3


def test_get_swap_chart_15m(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/swap-chart/1/15m/0/3000000000")
    response = r.json()
    assert r.status_code == 200
    assert len(response) == 4

    assert response[0][0] == 0
    assert response[0][1] == 1
    assert response[0][2] == 3
    assert response[0][3] == 3
    assert response[0][4] == 1
    assert response[0][5] == 3

    assert response[1][0] == 900000000
    assert response[1][1] == 3
    assert response[1][2] == 6
    assert response[1][3] == 6
    assert response[1][4] == 3
    assert response[1][5] == 3

    assert response[2][0] == 1800000000
    assert response[2][1] == 6
    assert response[2][2] == 6
    assert response[2][3] == 6
    assert response[2][4] == 6
    assert response[2][5] == 0

    assert response[3][0] == 2700000000
    assert response[3][1] == 6
    assert response[3][2] == 9
    assert response[3][3] == 9
    assert response[3][4] == 6
    assert response[3][5] == 3


def test_get_swap_chart_1h(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/swap-chart/2/1h/0/20000000000")
    response = r.json()
    assert r.status_code == 200
    assert len(response) == 6

    assert response[0][0] == 0
    assert response[0][1] == 1
    assert response[0][2] == 3
    assert response[0][3] == 3
    assert response[0][4] == 1
    assert response[0][5] == 3

    assert response[1][0] == 3600000000
    assert response[1][1] == 3
    assert response[1][2] == 6
    assert response[1][3] == 6
    assert response[1][4] == 3
    assert response[1][5] == 3

    assert response[2][0] == 7200000000
    assert response[2][1] == 6
    assert response[2][2] == 6
    assert response[2][3] == 6
    assert response[2][4] == 6
    assert response[2][5] == 0

    assert response[3][0] == 10800000000
    assert response[3][1] == 6
    assert response[3][2] == 9
    assert response[3][3] == 9
    assert response[3][4] == 6
    assert response[3][5] == 3


def test_get_swap_chart_4h(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/swap-chart/3/4h/0/50000000000")
    response = r.json()
    assert r.status_code == 200
    assert len(response) == 4

    assert response[0][0] == 0
    assert response[0][1] == 1
    assert response[0][2] == 3
    assert response[0][3] == 3
    assert response[0][4] == 1
    assert response[0][5] == 3

    assert response[1][0] == 14400000000
    assert response[1][1] == 3
    assert response[1][2] == 6
    assert response[1][3] == 6
    assert response[1][4] == 3
    assert response[1][5] == 3

    assert response[2][0] == 28800000000
    assert response[2][1] == 6
    assert response[2][2] == 6
    assert response[2][3] == 6
    assert response[2][4] == 6
    assert response[2][5] == 0

    assert response[3][0] == 43200000000
    assert response[3][1] == 6
    assert response[3][2] == 9
    assert response[3][3] == 9
    assert response[3][4] == 6
    assert response[3][5] == 3


def test_get_swap_chart_1d(prep_fixtures, client: TestClient) -> None:
    r = client.get(f"{settings.PREFIX}/dex/swap-chart/4/1d/0/300000000000")
    response = r.json()
    assert r.status_code == 200
    assert len(response) == 4

    assert response[0][0] == 0
    assert response[0][1] == 1
    assert response[0][2] == 3
    assert response[0][3] == 3
    assert response[0][4] == 1
    assert response[0][5] == 3

    assert response[1][0] == 86400000000
    assert response[1][1] == 3
    assert response[1][2] == 6
    assert response[1][3] == 6
    assert response[1][4] == 3
    assert response[1][5] == 3

    assert response[2][0] == 172800000000
    assert response[2][1] == 6
    assert response[2][2] == 6
    assert response[2][3] == 6
    assert response[2][4] == 6
    assert response[2][5] == 0

    assert response[3][0] == 259200000000
    assert response[3][1] == 6
    assert response[3][2] == 9
    assert response[3][3] == 9
    assert response[3][4] == 6
    assert response[3][5] == 3

