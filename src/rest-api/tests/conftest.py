import json
import os
from typing import Generator
from time import time

import pytest
from fastapi.testclient import TestClient

ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")
if ENVIRONMENT == "local":
    # `.env.local` should be ignored in dockerignore so as to fail in container
    os.environ["ENV_FILE"] = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), ".env.local"
    )

from app.db.session import MongoClient
from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c


def insert_fixture(fixture, collection_name=""):
    if collection_name == "":
        collection_name = fixture

    client = MongoClient

    # Read fixture
    with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fixtures", fixture + ".json"
        )
    ) as f:
        fixture_json = json.load(f)

    # Populate collection
    db = client["balanced"]
    db[collection_name].insert_many(fixture_json)

def insert_fixture_with_recent_timestamps(fixture, collection_name=""):
    if collection_name == "":
        collection_name = fixture

    client = MongoClient

    # Read fixture
    with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "fixtures", fixture + ".json"
        )
    ) as f:
        fixture_json = json.load(f)

    # edit timestamps
    # start 24 hours ago
    recent_time = (time() * 1000000) - 86400000000 + 300000000
    for f in fixture_json:
        f["timestamp"] = recent_time

        # 5 minute intervals
        recent_time += 300000000

    # Populate collection
    db = client["balanced"]
    db[collection_name].insert_many(fixture_json)



def delete_fixture(collection_name):
    client = MongoClient
    db = client["balanced"]

    db[collection_name].delete_many({})


@pytest.fixture()
def prep_fixtures():

    # Setup database
    insert_fixture("loans")
    insert_fixture("dex")
    insert_fixture("dex_swap_events")
    insert_fixture("collateral_chart")
    insert_fixture("loans_chart")
    insert_fixture("bnusd")

    # Run tests
    yield

    # Cleanup database
    delete_fixture("loans")
    delete_fixture("dex")
    delete_fixture("dex_swap_events")
    delete_fixture("collateral_chart")
    delete_fixture("loans_chart")
    delete_fixture("bnusd")

@pytest.fixture()
def prep_recent_fixtures():

    # Setup database
    insert_fixture_with_recent_timestamps("dex_swap_events")

    # Run tests
    yield

    # Cleanup database
    delete_fixture("dex_swap_events")

