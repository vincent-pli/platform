from pydantic import HttpUrl, Field, validator
from src.infrence.constants import TASKS_SUPPORTED
from src.models import ORJSONModel


class Launcher(ORJSONModel):
    name: str
    task: str
    model: str

    @validator("task")
    def valid_tasl(cls, task: str) -> str:
        if task not in TASKS_SUPPORTED:
            raise ValueError(
                "task is not validata or supported"
            )
        return task

class LaunchResponse(ORJSONModel):
    id: str
    address: HttpUrl