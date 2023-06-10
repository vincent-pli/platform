from datetime import datetime

from databases.interfaces import Record
from fastapi import Cookie, Depends

from src.infrence import service
from src.infrence.exceptions import InvalidMode
from src.infrence.schemas import Launcher


async def valid_launcher(launcher: Launcher) -> Launcher:
    if await service.get_model_by_name(launcher):
        raise InvalidMode()

    return launcher


# async def valid_refresh_token(
#     refresh_token: str = Cookie(..., alias="refreshToken"),
# ) -> Record:
#     db_refresh_token = await service.get_refresh_token(refresh_token)
#     if not db_refresh_token:
#         raise RefreshTokenNotValid()

#     if not _is_valid_refresh_token(db_refresh_token):
#         raise RefreshTokenNotValid()

#     return db_refresh_token


# async def valid_refresh_token_user(
#     refresh_token: Record = Depends(valid_refresh_token),
# ) -> Record:
#     user = await service.get_user_by_id(refresh_token["user_id"])
#     if not user:
#         raise RefreshTokenNotValid()

#     return user


# def _is_valid_refresh_token(db_refresh_token: Record) -> bool:
#     return datetime.utcnow() <= db_refresh_token["expires_at"]
