import asyncio
from typing import Any, AsyncGenerator, Dict

import edgedb
import pytest

from fastapiusers_edgedb import EdgeDBUserDatabase
from fastapiusers_edgedb.access_token import EdgeDBAccessTokenDatabase


class RollBack(Exception):
    pass


@pytest.fixture
async def edgedb_user_db(edgedb_db) -> AsyncGenerator[EdgeDBUserDatabase, None]:
    yield EdgeDBUserDatabase(edgedb_db)


@pytest.fixture
async def edgedb_user_db_oauth(edgedb_db) -> AsyncGenerator[EdgeDBUserDatabase, None]:
    yield EdgeDBUserDatabase(edgedb_db)


@pytest.fixture
async def edgedb_access_token_db(
    edgedb_db,
) -> AsyncGenerator[EdgeDBAccessTokenDatabase, None]:
    yield EdgeDBAccessTokenDatabase(edgedb_db)


@pytest.fixture(scope="session")
def event_loop():
    """Force the pytest-asyncio loop to be the main one."""
    loop = asyncio.get_event_loop()
    yield loop


@pytest.fixture
def oauth_account1() -> Dict[str, Any]:
    return {
        "oauth_name": "service1",
        "access_token": "TOKEN",
        "expires_at": 1579000751,
        "account_id": "7eb74a82-a036-11ed-bdbf-2f4754620f96",
        "account_email": "king.arthur@camelot.bt",
    }


@pytest.fixture
def oauth_account2() -> Dict[str, Any]:
    return {
        "oauth_name": "service2",
        "access_token": "TOKEN",
        "expires_at": 1579000751,
        "account_id": "7eb74a82-a036-11ed-bdbf-2f4754620f9i",
        "account_email": "king.arthur@camelot.bt",
    }


@pytest.fixture
async def edgedb_db() -> edgedb.AsyncIOClient:
    client = edgedb.create_async_client()
    try:
        async for tx in client.transaction():
            async with tx:
                yield tx
                raise RollBack
    except RollBack:
        pass
