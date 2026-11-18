# 资料验证

使用 Python 3.11+。在本目录创建并激活虚拟环境，然后运行：

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

访问 http://127.0.0.1:8000/docs，执行 `POST /profiles`，请求体为 `{"name":" 小林 ","age":20,"address":{"city":"上海"}}`。预期 HTTP 200，正文为 `{"name":"小林","age":20,"nickname":null,"address":{"city":"上海"},"tags":[]}`。ReDoc 位于 `/redoc`。

从仓库根目录运行 `python -m pytest fastapi/tests`。详情见[测试说明](../../tests/README.md)。
