from databases.interfaces import Record
from fastapi import APIRouter, BackgroundTasks, Depends, Response, status

from src.infrence import service
from src.infrence.dependencies import (
    valid_launcher
)
from src.auth.jwt import parse_jwt_user_data
from src.infrence.schemas import Launcher, LaunchResponse

router = APIRouter()


@router.post("/launch", status_code=status.HTTP_201_CREATED, response_model=LaunchResponse)
async def launch(
    launch_data: Launcher = Depends(valid_launcher),
) -> dict[str, str]:
    user = await service.launch(launch_data)
    return {
        "email": user["email"],  # type: ignore
    }






