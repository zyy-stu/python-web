"""用户资料输入合同。"""

from typing import Annotated

from pydantic import BaseModel, Field, field_validator


class Address(BaseModel):
    city: str = Field(min_length=1, max_length=40)


class Profile(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    age: int = Field(ge=18, le=120)
    nickname: str | None = None
    address: Address
    tags: list[Annotated[str, Field(min_length=1)]] = Field(default_factory=list)

    @field_validator("name", mode="before")
    @classmethod
    def strip_name(cls, value: object) -> object:
        return value.strip() if isinstance(value, str) else value
