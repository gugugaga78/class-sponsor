# -*- coding: utf-8 -*-
"""data.json -> data.js 同步脚本
每次修改 data.json 后运行：python sync_data.py
data.js 用于本地双击（file://）打开时绕过浏览器的 fetch 限制。
"""
import json

with open('data.json', encoding='utf-8') as f:
    data = json.load(f)

with open('data.js', 'w', encoding='utf-8') as f:
    f.write('window.__DASHBOARD_DATA__ = ')
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write(';\n')

total = sum(r['amount'] for r in data['records'])
print('同步完成：%d 笔流水，%d 名成员，金额合计 ¥%s'
      % (len(data['records']), len(data['students']), total))
