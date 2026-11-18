# FastAPI 开发任务

| 编号 | 标题 | 文件路径 | 前置知识 | 交付内容 | 验收标准 | 状态 |
| --- | --- | --- | --- | --- | --- | --- |
| FA-001 | FastAPI 介绍 | [docs/01-getting-started/01-introduction.md](docs/01-getting-started/01-introduction.md) | Python 基础 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-002 | 环境搭建 | [docs/01-getting-started/02-environment.md](docs/01-getting-started/02-environment.md) | FA-001 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-003 | 创建第一个 FastAPI 项目 | [docs/01-getting-started/03-first-api.md](docs/01-getting-started/03-first-api.md) | FA-002 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-004 | 启动服务与 API 文档 | [docs/01-getting-started/05-running-and-docs.md](docs/01-getting-started/05-running-and-docs.md) | FA-003 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-005 | 项目目录结构 | [docs/01-getting-started/04-project-structure.md](docs/01-getting-started/04-project-structure.md) | FA-004 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-006 | 路径操作与路由基础 | [docs/02-routing/00-routing-basics.md](docs/02-routing/00-routing-basics.md) | FA-005 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-007 | 路径参数 | [docs/02-routing/01-path-parameters.md](docs/02-routing/01-path-parameters.md) | FA-006 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-008 | 查询参数 | [docs/02-routing/02-query-parameters.md](docs/02-routing/02-query-parameters.md) | FA-007 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-009 | 请求体 | [docs/02-routing/03-request-body.md](docs/02-routing/03-request-body.md) | FA-008 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-010 | 路径参数与查询参数组合 | [docs/02-routing/04-multiple-parameters.md](docs/02-routing/04-multiple-parameters.md) | FA-009 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-011 | 响应模型 | [docs/02-routing/05-response.md](docs/02-routing/05-response.md) | FA-010 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-012 | 状态码与响应处理 | [docs/02-routing/06-status-codes.md](docs/02-routing/06-status-codes.md) | FA-011 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-013 | 路由分组与 APIRouter | [docs/02-routing/07-router-groups.md](docs/02-routing/07-router-groups.md) | FA-012 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-014 | Pydantic 模型基础 | [docs/03-pydantic/01-model-basics.md](docs/03-pydantic/01-model-basics.md) | FA-013 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-015 | Field 字段验证 | [docs/03-pydantic/02-field-validation.md](docs/03-pydantic/02-field-validation.md) | FA-014 | 中文教程、请求与示例 | 核对状态、响应和练习 | 已完成 |
| FA-016 | Depends 依赖注入 | `docs/04-dependency-injection/depends.md` | FA-015 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-017 | 依赖共享 | `docs/04-dependency-injection/shared-dependencies.md` | FA-016 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-018 | 类依赖 | `docs/04-dependency-injection/class-dependencies.md` | FA-017 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-019 | yield 依赖 | `docs/04-dependency-injection/yield-dependencies.md` | FA-018 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-020 | SQLAlchemy 集成 | `docs/05-database/sqlalchemy.md` | FA-019 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-021 | CRUD | `docs/05-database/crud.md` | FA-020 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-022 | 数据库迁移 | `docs/05-database/migrations.md` | FA-021 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-023 | JWT 认证 | `docs/06-authentication/jwt.md` | FA-022 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-024 | RBAC 权限 | `docs/06-authentication/rbac.md` | FA-023 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-025 | 中间件 | `docs/07-advanced/middleware.md` | FA-024 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-026 | 文件上传 | `docs/07-advanced/upload.md` | FA-025 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-027 | 后台任务 | `docs/07-advanced/background-tasks.md` | FA-026 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-028 | WebSocket | `docs/07-advanced/websocket.md` | FA-027 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-029 | 自动化测试 | `docs/08-testing/api-testing.md` | FA-028 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
| FA-030 | Docker 部署 | `docs/09-deployment/docker.md` | FA-029 | 机制讲解和独立示例 | 运行正常和失败请求并记录结果 | 待开发 |
