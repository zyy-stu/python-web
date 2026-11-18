# 参考答案

1. GET /health 返回 200，正文为 `{"status":"ok"}`。
2. GET /users?limit=0 返回 422，错误位置是 query.limit。
3. POST /profiles 提供姓名和年龄，省略 address 后返回 422，错误位置是 body.address。
