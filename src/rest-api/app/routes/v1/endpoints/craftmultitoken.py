from typing import Any
from fastapi import APIRouter, Depends, HTTPException

from app import crud
from app.core.config import settings

router = APIRouter()

from prometheus_client import Gauge

# Dict for prometheus metrics
metrics = {}


metrics["get_craft_multi_token_transactions"] = Gauge(
    "get_craft_multi_token_transactions",
    "requests to '/craft_multi_token/transactions'",
    ["network_name"],
)
@router.get("/transactions")
def get_transactions(
    *,
    limit: int = 1,
    skip: int = 0,
) -> Any:
    """
    Get transactions to the craft_multi_token contract
    """
    metrics["get_craft_multi_token_transactions"].labels(settings.NETWORK_NAME).inc()

    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be greater than 0")

    return crud.craft_multi_token.get_craft_multi_token_transactions(limit, skip)


metrics["get_craft_multi_token_transactions_by_method"] = Gauge(
    "get_craft_multi_token_transactions_by_method",
    "requests to '/craft_multi_token/transactions/{method}'",
    ["network_name"],
)
@router.get("/transactions/{method}")
def get_transactions_by_method(
    *,
    method: str,
    limit: int = 1,
    skip: int = 0,
) -> Any:
    """
    Get transactions to the craft_multi_token contract and filter by method
    """
    metrics["get_craft_multi_token_transactions_by_method"].labels(settings.NETWORK_NAME).inc()

    if method == "":
        raise HTTPException(status_code=400, detail="method required")
    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be greater than 0")

    return crud.craft_multi_token.get_craft_multi_token_transactions_by_method(method, limit)


metrics["get_craft_multi_token_logs"] = Gauge(
    "get_craft_multi_token_logs",
    "requests to '/craft_multi_token/logs'",
    ["network_name"],
)
@router.get("/logs")
def get_logs(
    *,
    limit: int = 1,
    skip: int = 0,
) -> Any:
    """
    Get logs to the craft_multi_token contract
    """
    metrics["get_craft_multi_token_logs"].labels(settings.NETWORK_NAME).inc()

    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be greater than 0")

    return crud.craft_multi_token.get_craft_multi_token_logs(limit, skip)


metrics["get_craft_multi_token_logs_by_method"] = Gauge(
    "get_craft_multi_token_logs_by_method",
    "requests to '/craft_multi_token/logs/{method}'",
    ["network_name"],
)
@router.get("/logs/{method}")
def get_logs(
    *,
    method: str,
    limit: int = 1,
    skip: int = 0,
) -> Any:
    """
    Get logs to the craft_multi_token contract by method
    """
    metrics["get_craft_multi_token_logs_by_method"].labels(settings.NETWORK_NAME).inc()

    if method == "":
        raise HTTPException(status_code=400, detail="method required")
    if limit <= 0:
        raise HTTPException(status_code=400, detail="limit must be greater than 0")

    return crud.craft_multi_token.get_craft_multi_token_logs_by_method(method, limit, skip)

