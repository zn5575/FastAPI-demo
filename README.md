# FastAPI-demo

这是一个基于 FastAPI 的 RESTful API 项目，用于实现用户注册和身份验证功能。

## 安装

1. 克隆此仓库：

   ```
   git clone https://github.com/zn5575/FastAPI-demo.git
   ```

2. 进入项目目录：

   ```
   cd FastAPI-demo
   ```

3. 创建并激活虚拟环境：

   ```
   python -m venv venv
   source venv/bin/
   ```

4. 安装依赖项：

   ```
   pip install -r requirements.txt
   ```

## 运行

1. 启动应用程序：

   ```
   uvicorn app.main:app --reload
   ```

2. 访问以下 以查看 API 文档：

   ```
   http://localhost:8000/docs
   ```

## 使用

### 注册用户

发送 POST 请求到 `/login/`，包含以下 JSON 数据：

```json
{
  "username": "user@example.com",
  "password": "password"
}
```

### 身验证

发送 POST 请求到 `/token/`，包含以下 JSON 数据：

```json
{
  "username": "user@example.com",
  "password": "password"
}
```

将返回一个 JSON Web Token（JWT），您可以使用它来访问需要身份验证的端点。

### 获取用户信息

发送 GET 请求到 `/users/me/`，并在请求头中包含以下内容：

```
Authorization: Bearer <JWT>
```

将返回一个 JSON 对象，其中包含有关当前用户的信息。

## 许可证

此项目根据 MIT 许可证进行许可。有关更多信息，请参见 LICENSE 文件。