# FA-014 Pydantic 模型基础

## 学习目标与前置知识

理解Pydantic 模型基础的用途，能够运行示例并解释请求结果。需要会运行 Python 命令和读写 JSON。建议先阅读[路由分组与 APIRouter](../02-routing/07-router-groups.md)。

## 基本概念与工作原理

BaseModel 由字段类型定义结构。name、age、address 必填；nickname 可为 None 且有默认值。可空类型在 Pydantic v2 中仍需显式默认值才允许省略。

## 安装与配置

需要 Python 3.11+。在 `fastapi/examples/03-pydantic` 中激活虚拟环境并安装该项目固定版本的依赖。三个 FastAPI 版本依赖分别为 FastAPI 0.159.1、Pydantic 2.14.1、Uvicorn 0.54.0。

```bash
python -m pip install -r requirements.txt
```

## 完整代码

本节使用下列完整项目文件。阅读入口后再查看本节涉及的实现 `schemas/user.py`。

- [main.py](../../examples/03-pydantic/main.py)
- [schemas/user.py](../../examples/03-pydantic/schemas/user.py)

## 运行命令

```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

## 请求示例

在 http://127.0.0.1:8000/docs 中执行以下请求。若用其他客户端，POST 的请求头为 `Content-Type: application/json`。

```http
POST /profiles
Host: 127.0.0.1:8000
Content-Type: application/json

{
  "name": " 小林 ",
  "age": 20,
  "address": {
    "city": "上海"
  }
}
```

## 响应示例

HTTP 200。

```json
{
  "name": "小林",
  "age": 20,
  "nickname": null,
  "address": {
    "city": "上海"
  },
  "tags": []
}
```

## 常见问题

若无法启动，先确认终端位于本示例目录，且 8000 端口可用。若响应不是预期结果，在 Swagger UI 检查请求使用的方法和参数，并确认没有同时运行其他示例占用该端口。

## 实际应用与练习

移除 nickname 后观察默认 null，再移除 address 验证必填。 记录请求、状态码和正文，并从仓库根目录执行 `python -m pytest fastapi/tests` 验证基线。

## 本章总结

先预测请求会如何被解析，再运行实验。根据状态码判断问题发生在路由匹配、请求校验或业务处理阶段。

## 参考资料与下一篇

[FastAPI 官方文档](https://fastapi.tiangolo.com/tutorial/body/) · [Pydantic 模型文档](https://docs.pydantic.dev/latest/concepts/models/)。

下一篇 [Field 字段验证](02-field-validation.md)。 [返回本章](README.md)。
