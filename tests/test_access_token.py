from datetime import datetime, timedelta, timezone
from typing import Any, AsyncGenerator

import pytest

from fastapiusers_edgedb.access_token import EdgeDBAccessTokenDatabase


@pytest.fixture
async def edgedb_access_token_db(
    edgedb_db,
) -> AsyncGenerator[EdgeDBAccessTokenDatabase, None]:
    yield EdgeDBAccessTokenDatabase(edgedb_db)


@pytest.fixture
def user_id() -> Any:
    return "user_id"


@pytest.mark.asyncio
async def test_queries(
    edgedb_access_token_db: EdgeDBAccessTokenDatabase,
    user_id: Any,
):
    access_token_create = {"token": "TOKEN", "user_id": user_id}

    # Create
    access_token = await edgedb_access_token_db.create(access_token_create)
    assert access_token.token == "TOKEN"
    assert access_token.user_id == user_id

    # Update
    update_dict = {"created_at": datetime.now(timezone.utc)}
    updated_access_token = await edgedb_access_token_db.update(
        access_token, update_dict
    )
    assert updated_access_token.created_at == update_dict["created_at"]

    # Get by token
    access_token_by_token = await edgedb_access_token_db.get_by_token(
        access_token.token
    )
    assert access_token_by_token is not None

    # Get by token expired
    access_token_by_token = await edgedb_access_token_db.get_by_token(
        access_token.token, max_age=datetime.now(timezone.utc) + timedelta(hours=1)
    )
    assert access_token_by_token is None

    # Get by token not expired
    access_token_by_token = await edgedb_access_token_db.get_by_token(
        access_token.token, max_age=datetime.now(timezone.utc) - timedelta(hours=1)
    )
    assert access_token_by_token is not None

    # Get by token unknown
    access_token_by_token = await edgedb_access_token_db.get_by_token(
        "NOT_EXISTING_TOKEN"
    )
    assert access_token_by_token is None

    # Delete token
    await edgedb_access_token_db.delete(access_token)
    deleted_access_token = await edgedb_access_token_db.get_by_token(access_token.token)
    assert deleted_access_token is None


@pytest.mark.asyncio
async def test_insert_existing_token(
    edgedb_access_token_db: EdgeDBAccessTokenDatabase,
    user_id: Any,
):
    access_token_create = {"token": "TOKEN", "user_id": user_id}
    await edgedb_access_token_db.create(access_token_create)

    with pytest.raises(Exception):
        await edgedb_access_token_db.create(access_token_create)
