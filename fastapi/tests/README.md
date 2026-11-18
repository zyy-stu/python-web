# API 测试

从仓库根目录运行 `python -m pip install -r fastapi/examples/01-hello-world/requirements.txt`，再运行 `python -m pytest fastapi/tests`。子进程在各示例目录导入同名的 main 模块，使用 TestClient 验证 JSON、状态码、校验定位和 API 文档。
