"""FastAPI Users database adapter for EdgeDB."""
import dataclasses
from typing import Any, Dict, Generic, Optional

from edgedb import AsyncIOClient
from fastapi_users.db.base import BaseUserDatabase
from fastapi_users.models import ID, OAP, UP

from fastapiusers_edgedb import user_api

__version__ = "0.1.0"


class EdgeDBUserDatabase(Generic[UP, ID], BaseUserDatabase[UP, ID]):
    """Database adapter for EdgeDB."""

    def __init__(self, client: AsyncIOClient):
        self.client = client

    async def get(self, id: ID) -> Optional[UP]:
        """Get a single user by id."""
        user: Optional[UP] = await user_api.get_user(
            self.client, cast="uuid", key="id", value=id
        )
        return user

    async def get_by_email(self, email: str) -> Optional[UP]:
        """Get a single user by email."""
        user: Optional[UP] = await user_api.get_user(
            self.client,
            cast="str",
            key="email ",
            value=str(email).lower(),
        )
        return user

    async def create(self, create_dict: Dict[str, Any]) -> UP:
        """Create a user."""
        user: UP = await user_api.create_user(self.client, **create_dict)
        return user

    async def update(self, user: UP, update_dict: Dict[str, Any]) -> UP:
        """Update a user."""
        user = await self.get(id=user.id)
        if user:
            user_dict = dataclasses.asdict(user)
            user_dict.update(update_dict)
            user = await user_api.update_user(
                self.client,
                **{
                    k: v
                    for k, v in user_dict.items()
                    if k not in ["id", "oauth_accounts"]
                }
            )
        return user

    async def delete(self, user: UP) -> None:
        """Delete a user."""
        await user_api.delete_user(self.client, id=user.id)

    async def add_oauth_account(self, user: UP, create_dict: Dict[str, Any]) -> UP:
        """Create an OAuth account and add it to the user."""
        user = await user_api.get_user(
            self.client, cast="uuid", key="id", value=user.id
        )
        if user:
            await user_api.add_oauth_account(
                self.client, user_id=user.id, **create_dict
            )
            user = await user_api.get_user(
                self.client, cast="uuid", key="id", value=user.id
            )
        return user

    async def get_by_oauth_account(self, oauth: str, account_id: str) -> Optional[UP]:
        """Get a single user by OAuth account id."""
        oauth_account = await user_api.get_by_oauth_account(
            self.client, oauth_name=oauth, account_id=account_id
        )
        return oauth_account

    async def update_oauth_account(
        self, user: UP, oauth_account: OAP, update_dict: Dict[str, Any]
    ) -> UP:
        """Update an OAuth account on a user."""
        user = await user_api.get_user(
            self.client, cast="uuid", key="id", value=user.id
        )
        if user:
            oauth_dict = dataclasses.asdict(oauth_account)
            oauth_dict.update(update_dict)
            await user_api.update_oauth_account(
                self.client,
                user_id=user.id,
                oauth_name=dataclasses.asdict(oauth_account)["oauth_name"],
                **{
                    k: v
                    for k, v in oauth_dict.items()
                    if k
                    in [
                        "access_token",
                        "expires_at",
                        "refresh_token",
                        "account_email",
                        "account_id",
                    ]
                }
            )
            user = await user_api.get_user(
                self.client, cast="uuid", key="id", value=user.id
            )
            # print("?????????????????????????????????????????")
            # print(user)
            # print("?????????????????????????????????????????")
        return user
