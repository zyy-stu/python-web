"""用户和产品路由入口。"""

from routers import products, users

from fastapi import FastAPI

app = FastAPI(title="路由示例")
app.include_router(users.router)
app.include_router(products.router)
