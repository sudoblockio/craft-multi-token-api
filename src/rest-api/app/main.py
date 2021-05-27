import logging
import uvicorn
from fastapi import FastAPI
from starlette_exporter import PrometheusMiddleware, handle_metrics
from multiprocessing.pool import ThreadPool


from app.core.config import settings
from app.routes.v1.router import api_router
from app.db.setup import index_mongo_collections

from prometheus_client import start_http_server

logging_level = logging.INFO
if settings.LOGGING_LEVEL == "CRITICAL":
    logging_level = logging.CRITICAL
elif settings.LOGGING_LEVEL == "ERROR":
    logging_level = logging.ERROR
elif settings.LOGGING_LEVEL == "WARNING":
    logging_level = logging.WARNING
elif settings.LOGGING_LEVEL == "INFO":
    logging_level = logging.INFO
elif settings.LOGGING_LEVEL == "DEBUG":
    logging_level = logging.DEBUG


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s :: %(levelname)s :: %(message)s"
)

tags_metadata = [
    {
        "name": "craft-multi-token",
        "description": settings.CRAFT_MULTI_TOKEN_CONTRACT_ADDRESS,
    },
]


app = FastAPI(
    title="CraftMultiToken REST API",
    description="...",
    version="v0.1.0",
    openapi_tags=tags_metadata,
    openapi_url=f"{settings.PREFIX}/openapi.json",
    docs_url=f"{settings.PREFIX}/docs",
)


@app.on_event("startup")
async def setup():
    # set up mongo
    index_mongo_collections()

    # Start prom server
    logging.info("Starting metrics server.")
    pool = ThreadPool(1)
    pool.apply_async(start_http_server, (settings.METRICS_PORT,settings.METRICS_ADDRESS))

app.include_router(api_router, prefix=settings.PREFIX)

app.add_middleware(
    PrometheusMiddleware, prefix="balanced_rest", app_name="balanced_rest", group_paths=True
)
app.add_route("/metrics", handle_metrics)
