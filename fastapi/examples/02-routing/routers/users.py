"""用户请求与公开响应模型。"""

from typing import Annotated

from pydantic import BaseModel, Field

from fastapi import APIRouter, HTTPException, Path, Query, status

router = APIRouter(prefix="/users", tags=["用户"])


class UserInput(BaseModel):
    name: str = Field(min_length=2, max_length=30)


class UserRead(BaseModel):
    id: int
    name: str


USERS = (UserRead(id=1, name="小林"), UserRead(id=2, name="小周"))


@router.get("", response_model=list[UserRead])
def list_users(limit: Annotated[int, Query(ge=1, le=20)] = 10) -> list[UserRead]:
    return list(USERS[:limit])


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: Annotated[int, Path(ge=1)],
    verbose: bool = False,
) -> dict[str, int | str]:
    for user in USERS:
        if user.id == user_id:
            return {"id": user.id, "name": user.name, "debug": "示例字段" if verbose else ""}
    raise HTTPException(status_code=404, detail="用户不存在")


@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserInput) -> UserRead:
    """演示创建响应，数据仅用于此次请求。"""
    return UserRead(id=3, name=payload.name)
