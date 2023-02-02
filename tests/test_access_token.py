import uuid
from datetime import datetime, timedelta, timezone
from typing import Any

import pytest

from fastapiusers_edgedb import EdgeDBUserDatabase
from fastapiusers_edgedb.access_token import EdgeDBAccessTokenDatabase


@pytest.fixture
async def user_id(
    edgedb_user_db: EdgeDBUserDatabase,
) -> uuid.UUID:
    user_create = {
        "email": "lancelot@camelot.bt",
        "hashed_password": "guinevere",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
    }

    user = await edgedb_user_db.create(user_create)
    return user.id


@pytest.mark.asyncio
async def test_queries(
    edgedb_access_token_db: EdgeDBAccessTokenDatabase,
    edgedb_user_db: EdgeDBUserDatabase,
    user_id: Any,
):
    access_token_create = {"token": "TOKEN", "user_id": user_id}

    # Create
    returned_obj = await edgedb_access_token_db.create(access_token_create)
    user = await edgedb_user_db.get(returned_obj[0])
    access_token = user.access_tokens[0]
    assert access_token.token == "TOKEN"

    # Update
    update_dict = {"created_at": datetime.now(timezone.utc)}
    returned_tuple = await edgedb_access_token_db.update(access_token, update_dict)
    user = await edgedb_user_db.get(returned_tuple[0])
    assert user.access_tokens[0].created_at == update_dict["created_at"]

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
    print("??????????????????", deleted_access_token)
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
