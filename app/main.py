from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import router
from app.database import models
from app.database.base import engine

# 初始化数据库
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# 添加路由
app.include_router(router)

# 添加跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
