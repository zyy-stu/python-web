# Python Web 开发教程

这是 Python Learning Roadmap 的中文 Web 专题，面向已掌握 Python 函数、模块、类型注解和虚拟环境的学习者。目标是从 HTTP 请求开始，完成可测试的 API，并逐步加入数据库、认证和部署。

## 知识体系与路线

1. 学习 [HTTP 与 REST API](common/rest-api/README.md)，掌握方法、路径和状态码。
2. 完成 [FastAPI 第一阶段](fastapi/docs/README.md)的入门、路由和数据验证，运行[三个示例](fastapi/examples/README.md)并核对[测试](fastapi/tests/README.md)。
3. 根据场景选择 [Django](django/README.md) 的完整站点路线或 [Flask](flask/README.md) 的轻量应用路线。
4. 学习[公共技术](common/README.md)，覆盖数据、认证、授权、安全、缓存与生产部署，再选择[实战项目](fastapi/projects/README.md)。

## 开发环境

Python 3.11+。每个示例包含固定运行依赖、独立启动说明和预期响应。根目录运行 `python -m pytest` 与 `python -m ruff check .`。参阅[贡献指南](CONTRIBUTING.md)、[规范](standards/README.md)及[教程模板](templates/README.md)。

项目采用 [MIT 许可证](LICENSE)。

## 其他专题

- [python-learning-roadmap](https://github.com/zyy-stu/python-learning-roadmap)
- [python-basic](https://github.com/zyy-stu/python-basic)
- [python-advanced](https://github.com/zyy-stu/python-advanced)
- [python-data-science](https://github.com/zyy-stu/python-data-science)
- [python-ai](https://github.com/zyy-stu/python-ai)
- [python-projects](https://github.com/zyy-stu/python-projects)
