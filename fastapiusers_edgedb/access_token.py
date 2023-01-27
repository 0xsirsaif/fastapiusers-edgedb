"""FastAPI Users access token database adapter for EdgeDB."""
import dataclasses
from datetime import datetime
from typing import Any, Dict, Generic, Optional

from edgedb import AsyncIOClient
from fastapi_users.authentication.strategy.db import AP, AccessTokenDatabase

from fastapiusers_edgedb import user_api


class EdgeDBAccessTokenDatabase(Generic[AP], AccessTokenDatabase[AP]):
    """Access token database adapter for EdgeDB."""

    def __init__(self, client: AsyncIOClient):
        self.client = client

    async def get_by_token(
        self, token: str, max_age: Optional[datetime] = None
    ) -> Optional[AP]:
        """Get a single access token by token."""
        access_token = await user_api.get_access_token(
            self.client, cast="str", key="token", value=token, max_age=max_age
        )
        return access_token

    async def create(self, create_dict: Dict[str, Any]) -> AP:
        """Create an access token."""
        access_token = await user_api.create_access_token(self.client, **create_dict)
        return access_token

    async def update(self, access_token: AP, update_dict: Dict[str, Any]) -> AP:
        """Update an access token."""
        access_token = await user_api.get_access_token(
            self.client, cast="str", key="token", value=access_token.token
        )
        if access_token:
            update_dict.update(dataclasses.asdict(access_token))
            access_token = await user_api.update_token(
                self.client, **{k: v for k, v in update_dict.items() if k not in ["id"]}
            )
        return access_token

    async def delete(self, access_token: AP) -> None:
        """Delete an access token."""
        await user_api.delete_token(self.client, token=access_token.token)
