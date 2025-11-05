codexgraph/
├── README.md
├── pyproject.toml                # 项目依赖定义（推荐使用 Poetry）
├── requirements.txt              # 兼容 pip 安装
├── setup.py                      # 可选：作为可安装包
├── .env.example                  # 环境变量示例
├── .gitignore
├── docker-compose.yml            # 本地服务编排 (Neo4j, Milvus, API)
├── Dockerfile                    # 主服务容器构建文件
├── Makefile                      # 常用命令（lint, test, run）
├── scripts/                      # 辅助脚本与工具
│   ├── init_db.py
│   ├── build_index.py
│   └── parse_repo.py
│
├── config/                       # 配置管理
│   ├── default.yaml
│   ├── dev.yaml
│   └── prod.yaml
│
├── codexgraph/                   # 主源码目录
│   ├── __init__.py
│
│   ├── core/                     # 核心引擎层
│   │   ├── __init__.py
│   │   ├── parser/               # 源代码解析 (tree-sitter等)
│   │   │   ├── base_parser.py
│   │   │   ├── python_parser.py
│   │   │   ├── java_parser.py
│   │   │   └── utils.py
│   │   ├── graph/                # 图存储/分析模块 (Neo4j接口)
│   │   │   ├── graph_builder.py
│   │   │   ├── graph_client.py
│   │   │   └── queries.py
│   │   ├── vector/               # 向量存储与检索
│   │   │   ├── vector_store.py
│   │   │   ├── embedding.py
│   │   │   └── retriever.py
│   │   ├── rag/                  # Graph + Vector RAG 引擎
│   │   │   ├── graph_rag.py
│   │   │   ├── prompt_templates.py
│   │   │   └── pipeline.py
│   │   ├── models/               # LLM 调用与模型接口
│   │   │   ├── openai_client.py
│   │   │   ├── local_llm.py
│   │   │   └── model_router.py
│   │   └── utils/                # 通用工具
│   │       ├── config_loader.py
│   │       ├── logger.py
│   │       ├── id_generator.py
│   │       └── text_splitter.py
│
│   ├── api/                      # RESTful / GraphQL API 层
│   │   ├── __init__.py
│   │   ├── main.py               # FastAPI 主入口
│   │   ├── routers/              # 路由划分
│   │   │   ├── graph.py
│   │   │   ├── vector.py
│   │   │   ├── llm.py
│   │   │   └── codebase.py
│   │   ├── schemas/              # Pydantic 数据模型
│   │   │   ├── graph_schema.py
│   │   │   └── llm_schema.py
│   │   └── deps.py               # 依赖注入 / 全局上下文
│
│   ├── services/                 # 后台服务与任务调度
│   │   ├── indexer_service.py    # 扫描 & 解析仓库
│   │   ├── embedding_service.py  # 向量化任务
│   │   ├── sync_service.py       # Git diff 增量更新
│   │   └── scheduler.py          # Celery / APScheduler 定时任务
│
│   ├── interfaces/               # 外部集成（GitHub、CI、监控等）
│   │   ├── github_client.py
│   │   ├── gitlab_client.py
│   │   ├── notifier.py
│   │   └── webhook_handler.py
│
│   └── app.py                    # 应用启动（入口聚合点）
│
├── tests/                        # 测试代码
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_graph.py
│   ├── test_vector.py
│   ├── test_rag.py
│   └── fixtures/
│
└── docs/                         # 项目文档
    ├── architecture.md
    ├── api_spec.md
    ├── design_decisions.md
    └── roadmap.md
