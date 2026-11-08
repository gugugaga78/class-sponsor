# 班级广告赞助透明看板

25级数智管理教改班 · 赞助进度公开透明

- 线上地址：https://gugugaga78.github.io/class-sponsor/
- 技术：纯静态 HTML + JSON 数据，GitHub Actions 自动部署到 Pages

## 文件说明

| 文件 | 作用 |
|---|---|
| `index.html` | 看板页面 |
| `data.json` | 数据源（线上唯一权威） |
| `data.js` | 内嵌数据副本，仅供本地双击打开时兜底，勿手改 |
| `sync_data.py` | 由 data.json 重新生成 data.js |

## 更新数据

1. 修改 `data.json`
2. 运行 `python sync_data.py`（同步本地兜底副本）
3. `git add . && git commit -m "更新赞助数据" && git push`
4. Actions 会自动更新线上页面

## 本地预览

- 直接双击 `index.html` 也能正常显示（走 data.js 兜底）
- 或起本地服务：`python -m http.server` 后访问 http://127.0.0.1:8000
