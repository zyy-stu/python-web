# FA-007 路径参数

## 学习目标与前置知识

理解路径参数的用途，能够运行示例并解释请求结果。需要会运行 Python 命令和读写 JSON。建议先阅读[路径操作与路由基础](00-routing-basics.md)。

## 基本概念与工作原理

路径占位符 user_id 与函数参数同名。FastAPI 将路径文本转换成整数，再应用 Path 的下限。资源不存在与参数非法分别处理。

## 安装与配置

需要 Python 3.11+。在 `fastapi/examples/02-routing` 中激活虚拟环境并安装该项目固定版本的依赖。三个 FastAPI 版本依赖分别为 FastAPI 0.159.1、Pydantic 2.14.1、Uvicorn 0.54.0。

```bash
python -m pip install -r requirements.txt
```

## 完整代码

本节使用下列完整项目文件。阅读入口后再查看本节涉及的实现 `routers/users.py`。

- [main.py](../../examples/02-routing/main.py)
- [routers/users.py](../../examples/02-routing/routers/users.py)
- [routers/products.py](../../examples/02-routing/routers/products.py)

## 运行命令

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

## 请求示例

在 http://127.0.0.1:8000/docs 中执行以下请求。若用其他客户端，POST 的请求头为 `Content-Type: application/json`。

```http
GET /users/1?verbose=true
Host: 127.0.0.1:8000
```

## 响应示例

HTTP 200。

```json
{
  "id": 1,
  "name": "小林"
}
```

## 常见问题

若无法启动，先确认终端位于本示例目录，且 8000 端口可用。若响应不是预期结果，在 Swagger UI 检查请求使用的方法和参数，并确认没有同时运行其他示例占用该端口。

## 实际应用与练习

请求 /users/nope 和 /users/99，比较 422 与 404；再试 /users/0。 记录请求、状态码和正文，并从仓库根目录执行 `python -m pytest fastapi/tests` 验证基线。

## 本章总结

先预测请求会如何被解析，再运行实验。根据状态码判断问题发生在路由匹配、请求校验或业务处理阶段。

## 参考资料与下一篇

[FastAPI 官方文档](https://fastapi.tiangolo.com/tutorial/path-params/)。

下一篇 [查询参数](02-query-parameters.md)。 [返回本章](README.md)。
