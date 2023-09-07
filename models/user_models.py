from enum import Enum
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Any, Dict


class Relationship(Enum):
    FAMILY = 0


class User(BaseModel):
    """
    Following best practices seen on MongoDB website:
    https://www.mongodb.com/developer/languages/python/flask-python-mongodb/
    """

    id: str
    name: str
    email: str
    relationships: Dict[str, Relationship]

    def to_json(self) -> Any:
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self) -> Any:
        return self.dict(by_alias=True, exclude_none=True)
