# AGENTS.md — 企业官网项目

## 项目概述

Django + Vue 3 企业官网系统。Django 提供 REST API 和管理后台，Vue 3 提供前台页面。

## 技术栈

| 层 | 技术 | 版本 |
|---|---|---|
| 后端框架 | Django | 5.2.16 |
| REST API | Django REST Framework | 3.17.1 |
| 跨域 | django-cors-headers | 4.9.0 |
| 后台主题 | django-simpleui | 2026.1.13 |
| 前端框架 | Vue 3 | 3.5.x |
| 构建工具 | Vite | 8.1.x |
| 路由 | Vue Router | 5.2.x |
| HTTP 客户端 | Axios | 1.18.x |
| Python | CPython | 3.11.9 |
| Node.js | | v26.4.0 |
| 数据库 | SQLite | (开发环境) |
| 语言 | 简体中文 | zh-hans |
| 时区 | Asia/Shanghai | |

## 目录结构

```
django企业官网/
├── config/              # Django 项目配置
│   ├── settings.py      # 全局设置（INSTALLED_APPS, MIDDLEWARE, DRF, CORS）
│   ├── urls.py          # 根路由（/ → website.urls, /admin/ → admin）
│   ├── wsgi.py / asgi.py
├── website/             # Django 主应用
│   ├── views.py         # API 视图（CompanyInfoView）
│   ├── urls.py          # API 路由（/api/info/）
│   ├── models.py        # 数据模型（待扩展）
│   ├── admin.py         # 后台注册（待扩展）
├── frontend/            # Vue 3 前端
│   ├── src/
│   │   ├── router/index.js   # 路由配置（/, /about, /contact）
│   │   ├── views/            # 页面组件（Home, About, Contact）
│   │   ├── App.vue           # 根组件（导航 + 路由视图 + 页脚）
│   │   ├── main.js           # 入口（挂载 router）
│   │   └── style.css         # 全局样式
│   ├── vite.config.js        # Vite 配置（含 API 代理）
│   └── package.json
├── venv/                # Python 虚拟环境
├── manage.py
└── db.sqlite3           # SQLite 数据库
```

## 开发环境启动

### 初始化（首次）

```powershell
# 激活 Python 虚拟环境
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
. .\venv\Scripts\Activate.ps1

# 安装前端依赖
cd frontend
npm install
cd ..
```

### 日常开发

```powershell
# 终端 1：启动 Django（端口 8000）
. .\venv\Scripts\Activate.ps1
python manage.py runserver

# 终端 2：启动 Vue 开发服务器（端口 5173）
cd frontend
npm run dev
```

### 访问地址

| 地址 | 说明 |
|---|---|
| http://localhost:5173 | Vue 企业官网前台 |
| http://127.0.0.1:8000/admin/ | Django simpleui 中文后台 |
| http://127.0.0.1:8000/api/info/ | 公司信息 API |

### 开发代理

Vite 开发服务器自动将 `/api/` 和 `/admin/` 请求代理到 Django (127.0.0.1:8000)，开发时无需关心跨域。

## API 端点

### GET /api/info/

返回公司基本信息。

```json
{
  "name": "企业官网",
  "description": "专注于企业数字化解决方案",
  "contact": {
    "address": "上海市浦东新区张江高科技园区",
    "phone": "021-8888-6666",
    "email": "contact@company.com"
  }
}
```

## Django 配置要点

- **INSTALLED_APPS 顺序**: `rest_framework` → `corsheaders` → `simpleui` → 默认 apps → `website`
- **MIDDLEWARE**: `CorsMiddleware` 必须在 `CommonMiddleware` 之前
- **CORS**: 开发环境 `CORS_ALLOW_ALL_ORIGINS = True`，生产需收紧
- **DRF**: 默认权限 `AllowAny`，生产需改为 `IsAuthenticated` 或按端点设置
- **语言**: `LANGUAGE_CODE = 'zh-hans'`
- **时区**: `TIME_ZONE = 'Asia/Shanghai'`

## 超级管理员

使用 `python manage.py createsuperuser` 创建，或在代码中创建后通过 Django shell 管理。

## 约定

1. **API 路由**: 统一放在 `website/urls.py`，通过 `config/urls.py` 以 `include()` 引入
2. **API 视图**: 优先使用 DRF 的 `APIView` 类视图
3. **Vue 页面**: 每个路由对应 `views/` 下一个 `.vue` 文件
4. **新增 Django app**: 使用 `python manage.py startapp <name>`，并在 `INSTALLED_APPS` 中注册
5. **数据库迁移**: 修改模型后执行 `python manage.py makemigrations && python manage.py migrate`
6. **静态资源**: 前端图片/字体等放 `frontend/public/`
