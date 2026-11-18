"""产品列表。"""

from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["产品"])


@router.get("")
def list_products() -> list[dict[str, str]]:
    return [{"name": "笔记本"}]
