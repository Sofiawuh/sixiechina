markdown
# 华为云代理商企业官网

![华为云](https://img.shields.io/badge/华为云-金牌代理商-FF6A00.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web框架-green.svg)
![Nginx](https://img.shields.io/badge/Nginx-反向代理-009639.svg)

## 🌟 项目简介

基于 Flask 框架构建的华为云代理商企业官方网站，展示公司作为华为云认证代理商的专业服务能力和行业解决方案。

## 🚀 快速开始

### 环境要求
- Python 3.x
- Flask 框架
- Nginx (生产环境)

### 安装运行

1. **安装依赖**
```bash
pip install -r requirements.txt
```

2. **运行开发服务器**
```bash
python app.py
```

3. **访问应用**
打开浏览器访问：`http://localhost:5000`

### 生产环境部署

1. **配置 Nginx**
```bash
# 使用项目中的 nginx.conf 配置
sudo cp nginx.conf /etc/nginx/sites-available/your_site
sudo ln -s /etc/nginx/sites-available/your_site /etc/nginx/sites-enabled/
```

2. **重启 Nginx**
```bash
sudo systemctl restart nginx
```

## 📁 项目结构

```
.
├── app.py                 # Flask 主应用文件
├── requirements.txt       # Python 依赖包
├── nginx.conf            # Nginx 配置文件
├── README.md             # 项目说明文档
├── ai_conversations.log  # AI对话日志
├── static/               # 静态资源目录
│   ├── css/
│   │   └── style.css     # 样式文件
│   ├── js/
│   │   ├── main.js       # 主JavaScript文件
│   │   └── remove-float-sidebar.js  # 侧边栏处理脚本
│   └── img/              # 图片资源
│       ├── sixie.png     # 公司Logo
│       ├── 工业banner.jpg
│       ├── 工业数字化.jpg
│       └── 华为云相关图片...
└── templates/            # HTML模板文件
    ├── base.html         # 基础模板
    ├── index.html        # 首页
    ├── about.html        # 关于我们
    ├── service.html      # 服务介绍
    ├── case.html         # 成功案例
    ├── news.html         # 新闻动态
    ├── contact.html      # 联系我们
    ├── 行业解决方案页面...
    └── 日期版本页面...
```

## 🎯 网站功能

### 主要页面
- **首页** (`index.html`) - 公司介绍和核心业务展示
- **关于我们** (`about.html`) - 公司背景和资质认证
- **服务介绍** (`service.html`) - 华为云产品和服务
- **成功案例** (`case.html`) - 行业解决方案案例
- **新闻动态** (`news.html`) - 最新资讯和活动
- **联系我们** (`contact.html`) - 联系信息和合作方式

### 行业解决方案
- **工业制造** (`mnft.html`) - 制造业数字化转型
- **金融服务** (`bank.html`) - 金融行业云解决方案
- **医疗健康** (`smarthealthcare.html`) - 智慧医疗
- **汽车行业** (`car.html`) - 汽车产业云服务
- **政府机构** (`gonc.html`) - 政务云平台
- **MaaS服务** (`maas.html`) - 模型即服务

## 🛠️ 技术架构

### 后端技术
- **Flask** - Python Web 框架
- **WSGI** - Web 服务器网关接口

### 前端技术
- **HTML5** - 页面结构
- **CSS3** - 样式设计
- **JavaScript** - 交互功能
- **响应式设计** - 多设备适配

### 部署环境
- **Nginx** - Web 服务器和反向代理
- **Gunicorn** - Python WSGI HTTP 服务器 (可选)

## 📦 依赖包

项目依赖包详见 `requirements.txt` 文件，主要包含：
- Flask
- 其他相关Python包

## 🔧 配置说明

### Nginx 配置
项目提供 `nginx.conf` 配置文件，包含：
- 静态文件服务
- 反向代理设置
- Gzip 压缩配置
- 缓存策略

### 静态资源
- CSS 文件：`static/css/`
- JavaScript 文件：`static/js/`
- 图片资源：`static/img/`

## 📞 联系我们

### 商务合作
- **公司官网**: [www.sixiechina.com]
- **联系电话**: [0755-26406163 转 803 ｜ 801]
- **邮箱地址**: [wuh@sixiechina.com]

### 技术支持
如需技术支持，请联系我们的技术团队。

## 🏆 我们的优势

作为华为云金牌代理商，我们提供：
- 专业的云服务咨询
- 定制化解决方案
- 7×24小时技术支持
- 丰富的行业经验

## 📄 许可证

本项目仅限内部使用。

---

<div align="center">

**专业云服务 · 值得信赖的合作伙伴**

*让云计算助力企业数字化转型*

</div>


