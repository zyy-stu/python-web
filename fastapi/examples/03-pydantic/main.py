"""验证嵌套用户资料并返回 JSON。"""

from schemas.user import Profile

from fastapi import FastAPI

app = FastAPI(title="用户资料示例")


@app.post("/profiles", response_model=Profile)
def preview_profile(payload: Profile) -> dict[str, object]:
    return payload.model_dump(mode="json")
