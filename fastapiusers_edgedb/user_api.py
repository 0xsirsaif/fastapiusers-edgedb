from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import List

import edgedb
from fastapi_users.authentication.strategy.db import AP
from fastapi_users.models import ID, UP


async def create_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    email: str,
    hashed_password: str,
    is_active: bool = True,
    is_superuser: bool = False,
    is_verified: bool = False,
) -> UP:
    return await executor.query_single(
        """\
        with
          email := <str>$email,
          is_active := <bool>$is_active,
          is_superuser := <bool>$is_superuser,
          is_verified := <bool>$is_verified,
          hashed_password := <str>$hashed_password
        select (
          insert User {
            email := email,
            is_active := is_active,
            is_superuser := is_superuser,
            is_verified := is_verified,
            hashed_password := hashed_password
          }
        ) {id, email, is_active, is_superuser, is_verified};\
        """,
        email=email,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
        hashed_password=hashed_password,
    )


async def get_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    cast: str,
    key: str,
    value: str | ID,
) -> UP:
    return await executor.query_single(
        f"""
        select User {{
            id, email, is_active, is_superuser, is_verified, hashed_password,
            oauth_accounts: {{
                access_token,
                expires_at,
                refresh_token,
                account_email,
                oauth_name,
                account_id,
            }},
            access_tokens: {{
                token,
                created_at,
            }}
        }}
        filter .{key} = <{cast}>'{value}';
    """
    )


async def update_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    email: str,
    is_active: bool,
    is_superuser: bool,
    is_verified: bool,
    hashed_password: str,
) -> UP | None:
    return await executor.query_single(
        """\
        with
          email := <str>$email,
          is_active := <bool>$is_active,
          is_superuser := <bool>$is_superuser,
          is_verified := <bool>$is_verified,
          hashed_password := <str>$hashed_password
        select (
            update User filter .email = <str>$email
            set {
                email := email,
                is_active := is_active,
                is_superuser := is_superuser,
                is_verified := is_verified,
                hashed_password := hashed_password
            }
        ) {id, email, is_active, is_superuser, is_verified};\
        """,
        email=email,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
        hashed_password=hashed_password,
    )


async def delete_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    id: uuid.UUID,
) -> UP | None:
    return await executor.query_single(
        """\
        with user := (delete User filter .id = <uuid>$id)
        select user {id, email, is_active, is_superuser, is_verified};\
        """,
        id=id,
    )


async def get_by_oauth_account(
    executor: edgedb.AsyncIOExecutor, *, account_id: str, oauth_name: str
) -> UP:
    return await executor.query_single(
        """\
        select User {
            id, is_active, is_superuser, is_verified, hashed_password,
            oauth_accounts: {
                access_token,
                expires_at,
                refresh_token,
                account_email,
                oauth_name,
                account_id,
            }
        }
        filter contains(User.oauth_accounts.oauth_name, <str>$oauth_name)
        and
        contains(User.oauth_accounts.account_id, <str>$account_id)
        limit 1
        """,
        oauth_name=oauth_name,
        account_id=account_id,
    )


async def insert_oauth_account(
    executor: edgedb.AsyncIOExecutor,
    *,
    oauth_name: str,
    access_token: str,
    expires_at: int,
    refresh_token: str,
    account_id: str,
    account_email: str,
) -> UP:
    return await executor.query_single(
        """\
        with
          oauth_name := <str>$oauth_name,
          access_token := <str>$access_token,
          expires_at := <int32>$expires_at,
          refresh_token := <str>$refresh_token,
          account_id := <str>$account_id,
          account_email := <str>$account_email,
        select (
            insert OAuthUser {
                oauth_name := oauth_name,
                access_token := access_token,
                expires_at := expires_at,
                refresh_token := refresh_token,
                account_email := account_email,
                account_id := account_id,
            }
        ) {oauth_name, access_token, expires_at, refresh_token, account_id};\
        """,
        oauth_name=oauth_name,
        access_token=access_token,
        expires_at=expires_at,
        refresh_token=refresh_token,
        account_id=account_id,
        account_email=account_email,
    )


async def add_oauth_account(
    executor: edgedb.AsyncIOExecutor,
    *,
    user_id: uuid.UUID,
    oauth_name: str,
    access_token: str,
    expires_at: int,
    refresh_token: str = "",
    account_id: int,
    account_email: str,
) -> UP:
    return await executor.query_single(
        """\
        with
            user_id := <uuid>$user_id,
            account := (
                insert OAuthUser {
                    oauth_name := <str>$oauth_name,
                    access_token := <str>$access_token,
                    expires_at := <int32>$expires_at,
                    refresh_token := <str>$refresh_token,
                    account_email := <str>$account_email,
                    account_id := <str>$account_id,
                }
            ),
            user := (
              update User filter .id = <uuid>$user_id
              set {
                oauth_accounts += account
              }
            )
        select (user_id, account, user)\
        """,
        user_id=user_id,
        oauth_name=oauth_name,
        access_token=access_token,
        expires_at=expires_at,
        refresh_token=refresh_token,
        account_email=account_email,
        account_id=account_id,
    )


async def update_oauth_account(
    executor: edgedb.AsyncIOExecutor,
    user_id: uuid.UUID,
    oauth_name: str,
    *,
    access_token: str = "",
    expires_at: int = 0,
    refresh_token: str = "",
    account_id: str = "",
    account_email: str = "",
):
    return await executor.query(
        """
    with
        user_id := <uuid>$user_id,
        updated_account := (
                update OAuthUser
                filter .oauth_name = <str>$oauth_name
                set {
                  oauth_name := <str>$oauth_name,
                  access_token := <str>$access_token,
                  expires_at := <int32>$expires_at,
                  refresh_token := <str>$refresh_token,
                  account_email := <str>$account_email,
                  account_id := <str>$account_id,
                }
        ),
        user := (
                update User
                filter .id = <uuid>$user_id
                set {
                    oauth_accounts += (
                      updated_account
                    )
                }
        )
        select (user_id, user, updated_account)
    """,
        user_id=user_id,
        oauth_name=oauth_name,
        access_token=access_token,
        expires_at=expires_at,
        refresh_token=refresh_token,
        account_email=account_email,
        account_id=account_id,
    )


async def get_access_token(
    executor: edgedb.AsyncIOExecutor,
    *,
    cast: str,
    key: str,
    value: str,
    max_age: datetime | None = datetime.now(timezone.utc),
) -> AP | None:
    date_filter = f"and .created_at >= <datetime>'{max_age}'" if max_age else ""
    return await executor.query_single(
        f"""
        select EdgeAccessTokenUser {{
            token, created_at
        }}
        filter .{key} = <{cast}>'{value}'
        {date_filter};
    """
    )


async def get_user_by_access_token(
    executor: edgedb.AsyncIOExecutor, access_token: str
) -> List[UP]:
    return await executor.query(
        f"""
        select User {{
            id,
            access_tokens: {{
                token, created_at
            }}
        }} filter .access_tokens.token = <str>$access_token
    """,
        access_token=access_token,
    )


async def create_access_token(
    executor: edgedb.AsyncIOExecutor,
    token: str,
    user_id: str,
    created_at: datetime = datetime.now(timezone.utc),
) -> AP:
    return await executor.query_single(
        """
        with
            user_id := <uuid>$user_id,
            access_token := (
                insert EdgeAccessTokenUser {
                    token := <str>$token,
                    created_at := <datetime>$created_at,
                }
            ),
            user := (
              update User filter .id = <uuid>$user_id
              set {
                access_tokens += access_token
              }
            )

        select (user_id, access_token, user)
    """,
        token=token,
        created_at=created_at,
        user_id=user_id,
    )


async def update_token(
    executor: edgedb.AsyncIOExecutor,
    user_id: uuid.UUID,
    token: str,
    created_at: datetime = datetime.now(timezone.utc),
) -> AP:
    return await executor.query_single(
        """
        with
            user_id := <uuid>$user_id,
            updated_access_token := (
                update EdgeAccessTokenUser filter .token = <str>$token
                set {
                  token := <str>$token,
                  created_at := <datetime>$created_at,
                }
            ),
            user := (
                update User filter .id = <uuid>$user_id
                set {
                    access_tokens += (
                      updated_access_token
                    )
                }
            )
        select (user_id, updated_access_token, user)
    """,
        user_id=user_id,
        token=token,
        created_at=created_at,
    )


async def delete_token(executor: edgedb.AsyncIOExecutor, token: str):
    user = await get_user_by_access_token(executor, token)
    user_id = user[0].id
    return await executor.query(
        """
        update User filter .id = <uuid>$user_id
        set {
            access_tokens -= (delete EdgeAccessTokenUser filter .token = <str>$token)
        }
    """,
        token=token,
        user_id=user_id,
    )
