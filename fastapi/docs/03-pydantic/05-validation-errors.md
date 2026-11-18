# 验证错误

## 学习目标与前置知识

理解验证错误的用途，能够运行示例并解释请求结果。需要会运行 Python 命令和读写 JSON。建议先阅读[模型序列化](04-model-serialization.md)。

## 基本概念与工作原理

FastAPI 将请求校验错误转换为 HTTP 422。detail 数组中的 loc 表示参数来源和字段位置，type 给出错误类别；不要让调用方依赖本地化错误文案。

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
  "name": "小林",
  "age": 17,
  "address": {
    "city": "上海"
  }
}
```

## 响应示例

HTTP 422。下列为对应校验位置和错误上下文。

```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": [
        "body",
        "age"
      ],
      "msg": "Input should be greater than or equal to 18",
      "input": 17,
      "ctx": {
        "ge": 18
      }
    }
  ]
}
```

## 常见问题

若无法启动，先确认终端位于本示例目录，且 8000 端口可用。若响应不是预期结果，在 Swagger UI 检查请求使用的方法和参数，并确认没有同时运行其他示例占用该端口。

## 实际应用与练习

使用错误的年龄和缺失城市，逐条检查错误定位。 记录请求、状态码和正文，并从仓库根目录执行 `python -m pytest fastapi/tests` 验证基线。

## 本章总结

先预测请求会如何被解析，再运行实验。根据状态码判断问题发生在路由匹配、请求校验或业务处理阶段。

## 参考资料与下一篇

[FastAPI 官方文档](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [Pydantic 模型文档](https://docs.pydantic.dev/latest/concepts/models/)。

下一阶段 [依赖注入导读](../04-dependency-injection/README.md)。 [返回本章](README.md)。
