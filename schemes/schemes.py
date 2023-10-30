from pydantic import BaseModel
from typing import Annotated, Dict
from annotated_types import MinLen, MaxLen


class ProjectScheme(BaseModel):
    code: int
    project_name: Annotated[str, MinLen(1), MaxLen(100)]
    project_data: Dict
