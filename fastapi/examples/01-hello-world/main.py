"""入门服务。"""

from fastapi import FastAPI

app = FastAPI(title="入门示例")


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "你好，FastAPI"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
