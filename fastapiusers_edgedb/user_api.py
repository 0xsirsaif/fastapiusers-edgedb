from __future__ import annotations

import uuid
from datetime import datetime, timezone

import edgedb
from fastapi_users.authentication.strategy.db import AP
from fastapi_users.models import UP


async def create_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    is_active: bool,
    is_superuser: bool,
    is_verified: bool,
    hashed_password: str,
) -> UP:
    return await executor.query_single(
        """\
        with
          first_name := <str>$first_name,
          last_name := <str>$last_name,
          username := <str>$username,
          email := <str>$email,
          is_active := <bool>$is_active,
          is_superuser := <bool>$is_superuser,
          is_verified := <bool>$is_verified,
          hashed_password := <str>$hashed_password
        select (
          insert EdgeBaseUser {
            first_name := first_name,
            last_name := last_name,
            username := username,
            email := email,
            is_active := is_active,
            is_superuser := is_superuser,
            is_verified := is_verified,
            hashed_password := hashed_password
          }
        ) {first_name, last_name, username, email, is_active, is_superuser, is_verified};\
        """,
        first_name=first_name,
        last_name=last_name,
        username=username,
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
    value: str,
) -> UP | None:
    return await executor.query_single(
        f"""
        select EdgeBaseUser {{
            first_name, last_name, username, email,
            is_active, is_superuser, is_verified, hashed_password,
            oauth_accounts: {{
                access_token,
                expires_at,
                refresh_token,
                account_email,
                oauth_name,
                account_id,
            }}
        }}
        filter .{key} = <{cast}>'{value}';
    """
    )


async def update_user(
    executor: edgedb.AsyncIOExecutor,
    *,
    first_name: str,
    last_name: str,
    username: str,
    email: str,
    is_active: bool,
    is_superuser: bool,
    is_verified: bool,
    hashed_password: str,
) -> UP | None:
    return await executor.query_single(
        """\
        with
          first_name := <str>$first_name,
          last_name := <str>$last_name,
          username := <str>$username,
          email := <str>$email,
          is_active := <bool>$is_active,
          is_superuser := <bool>$is_superuser,
          is_verified := <bool>$is_verified,
          hashed_password := <str>$hashed_password
        select (
            update EdgeBaseUser filter .username = <str>$username
            set {
                first_name := first_name,
                last_name := last_name,
                username := username,
                email := email,
                is_active := is_active,
                is_superuser := is_superuser,
                is_verified := is_verified,
                hashed_password := hashed_password
            }
        ) {first_name, last_name, username, email, is_active, is_superuser, is_verified};\
        """,
        first_name=first_name,
        last_name=last_name,
        username=username,
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
        with user := (delete EdgeBaseUser filter .id = <uuid>$id)
        select user {first_name, last_name, username, email, is_active, is_superuser, is_verified};\
        """,
        id=id,
    )


async def get_by_oauth_account(
    executor: edgedb.AsyncIOExecutor, *, account_id: str, oauth_name: str
) -> UP:
    return await executor.query_single(
        """\
        select EdgeBaseUser {
            first_name, last_name, username, email,
            is_active, is_superuser, is_verified, hashed_password,
            oauth_accounts: {
                access_token,
                expires_at,
                refresh_token,
                account_email,
                oauth_name,
                account_id,
            }
        }
        filter contains(EdgeBaseUser.oauth_accounts.oauth_name, <str>$oauth_name)
        and
        contains(EdgeBaseUser.oauth_accounts.account_id, <str>$account_id)
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
            insert EdgeBaseOAuthUser {
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
                insert EdgeBaseOAuthUser {
                    oauth_name := <str>$oauth_name,
                    access_token := <str>$access_token,
                    expires_at := <int32>$expires_at,
                    refresh_token := <str>$refresh_token,
                    account_email := <str>$account_email,
                    account_id := <str>$account_id,
                }
            ),
            user := (
              update EdgeBaseUser filter .id = <uuid>$user_id
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
    return await executor.query_single(
        """
    with
        user_id := <uuid>$user_id,
        updated_account := (
                update EdgeBaseOAuthUser
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
                update EdgeBaseUser
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
    max_age: datetime = None,
) -> AP | None:
    date_filter = f"and .created_at >= <datetime>'{max_age}'" if max_age else ""
    return await executor.query_single(
        f"""
        select EdgeAccessTokenUser {{
            token, created_at, user_id
        }}
        filter .{key} = <{cast}>'{value}'
        {date_filter};
    """
    )


async def create_access_token(
    executor: edgedb.AsyncIOExecutor,
    token: str,
    user_id: str,
    created_at: datetime = datetime.now(timezone.utc),
) -> AP:
    return await executor.query_single(
        """
        select (
            insert EdgeAccessTokenUser {
                token := <str>$token,
                created_at := <datetime>$created_at,
                user_id := <str>$user_id,
            }
        ) {token, created_at, user_id}
    """,
        token=token,
        created_at=created_at,
        user_id=user_id,
    )


async def update_token(
    executor: edgedb.AsyncIOExecutor,
    token: str,
    user_id: str,
    created_at: datetime = datetime.now(timezone.utc),
) -> AP:
    return await executor.query_single(
        """
        select (
            update EdgeAccessTokenUser filter .token = <str>$token
            set {
                token := <str>$token,
                created_at := <datetime>$created_at,
                user_id := <str>$user_id,
            }
        ) {token, created_at, user_id}
    """,
        token=token,
        created_at=created_at,
        user_id=user_id,
    )


async def delete_token(executor: edgedb.AsyncIOExecutor, token: str):
    return await executor.query(
        """
        delete EdgeAccessTokenUser
        filter .token = <str>$token
    """,
        token=token,
    )
