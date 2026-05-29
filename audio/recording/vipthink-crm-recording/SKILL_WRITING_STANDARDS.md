# Skill 编写规范

> 本文档定义了 VIPThink 团队 Skill 开发的编写规范，确保代码质量、可维护性和团队协作效率。

---

## 1. Skill 基本结构

```
skill-name/
├── SKILL.md              # 技能定义文件（核心，必须）
├── README.md             # 使用说明（对外分享时必须）
├── _meta.json            # 版本元信息
├── .gitignore            # Git 排除规则
├── scripts/              # 脚本文件（可选）
│   └── *.py / *.js / *.sh
├── references/           # 参考文档（可选）
│   └── *.md
├── examples/             # 示例输入输出（可选）
│   └── *.md
├── tests/                # 测试用例（可选）
│   └── *.md
└── data/                 # 数据文件（可选）
    └── *.yaml / *.json
```

---

## 2. SKILL.md 编写规范

### 2.1 Front Matter（头部元信息）

```yaml
---
name: skill-name                    # 技能唯一标识（kebab-case）
description: |
  一句话描述技能功能。               # 2-3 行，简洁明了
  包含核心能力和适用场景。
  当用户提到 XXX 时使用此技能。      # 列出触发关键词
---
```

**要求：**
- `name` 使用 `kebab-case` 命名（如 `crm-recording`）
- `description` 必须包含**触发关键词**，确保 AI 能正确识别调用
- 触发关键词要覆盖用户可能使用的各种说法

### 2.2 文档结构

```markdown
# 技能名称

## 概述
## 核心功能
## 系统信息 / 配置
## 使用指南
## 工作流程
## 故障排除
## 版本历史
```

### 2.3 编写原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **结构化** | 使用表格、列表、代码块组织信息 | 系统信息用表格，流程用编号列表 |
| **可操作** | 每个步骤都有明确的操作指令 | "点击 X 按钮" 而非 "进行操作" |
| **有示例** | 关键操作提供代码示例 | JavaScript 代码块、Python 代码块 |
| **标注风险** | 明确标注禁止操作和常见错误 | ❌ 禁止 / ⚠️ 注意 / ✅ 推荐 |
| **版本记录** | 每次重大更新记录版本历史 | 日期 + 版本号 + 变更内容 |

---

## 3. 敏感信息处理规范

### 3.1 禁止硬编码

```python
# ❌ 禁止：硬编码凭证
CRM_USERNAME = "18501099917"
API_KEY = "sk-99f9364af58c49d5b927f43dc08e2e5c"

# ✅ 推荐：从环境变量读取
CRM_USERNAME = os.environ.get("CRM_USERNAME", "")
API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")
```

### 3.2 占位符格式

统一使用 `<YOUR_XXX>` 格式：

| 类型 | 占位符 |
|------|--------|
| 账号 | `<YOUR_CRM_USERNAME>` |
| 密码 | `<YOUR_CRM_PASSWORD>` |
| API Key | `<YOUR_DASHSCOPE_API_KEY>` |
| Token | `<YOUR_ACCESS_TOKEN>` |
| URL | `<YOUR_SERVER_URL>` |

### 3.3 配置说明

在 README 或 SKILL.md 中必须说明凭证配置方式：

```markdown
## 配置说明

在使用前，请配置以下环境变量：

| 变量名 | 说明 | 获取方式 |
|--------|------|---------|
| CRM_USERNAME | CRM 登录账号 | 联系管理员 |
| CRM_PASSWORD | CRM 登录密码 | 联系管理员 |
| DASHSCOPE_API_KEY | 阿里云 API Key | 阿里云控制台 |
```

---

## 4. 代码规范

### 4.1 Python 脚本

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本功能说明（一句话）
"""

import os
import sys

# 常量定义（大写）
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

def main():
    """主函数"""
    pass

if __name__ == "__main__":
    main()
```

**要求：**
- 文件头包含编码声明 `# -*- coding: utf-8 -*-`
- 函数和类添加 docstring
- 常量使用大写命名
- 错误处理使用 try-except，不静默吞异常

### 4.2 JavaScript 代码块

在 SKILL.md 中的 JavaScript 示例：

```javascript
// 使用清晰的注释说明每一步
// 1. 找到目标元素
const buttons = document.querySelectorAll('button');
// 2. 遍历并点击
for (let btn of buttons) {
    if (btn.innerText.includes('查询')) {
        btn.click();
        break;
    }
}
```

---

## 5. 故障排除编写规范

### 5.1 错误分类

按严重程度和类型分类：

| 类别 | 说明 | 示例 |
|------|------|------|
| A 类 | CRM 操作类（高） | DOM 选择器失效 |
| B 类 | 连接类（高） | Chrome CDP 连接失败 |
| C 类 | API 调用类（中-高） | 认证失败 |
| D 类 | 分析类（中） | ASR 转录失败 |
| E 类 | 脚本工程类（中） | 语法错误 |

### 5.2 错误记录格式

```markdown
| 编号 | 错误描述 | 表现 | 正确做法 |
|------|---------|------|---------|
| A1 | 简洁描述 | 具体表现 | 修复方法 |
```

---

## 6. 版本管理规范

### 6.1 版本号规则

采用 `主版本.次版本` 格式：

| 变更类型 | 版本号变化 | 示例 |
|---------|-----------|------|
| 重大更新（新功能、架构变更） | 主版本 +1 | 5.0 → 6.0 |
| 功能增强（新增流程、优化） | 次版本 +1 | 6.0 → 6.1 |
| Bug 修复 | 不变，记录在版本历史中 | 6.0 (修复记录) |

### 6.2 版本历史格式

```markdown
| 日期 | 版本 | 内容 |
|------|------|------|
| 2026-05-29 | 7.0 | **重大更新**：(1)新增XXX；(2)修复XXX |
```

---

## 7. 上传前检查清单

### 7.1 内容完整性

- [ ] SKILL.md 包含完整的 front matter
- [ ] 触发关键词覆盖充分
- [ ] 核心功能有详细说明
- [ ] 故障排除覆盖已知问题
- [ ] 版本历史已更新

### 7.2 安全性

- [ ] 无硬编码凭证（账号、密码、API Key）
- [ ] 敏感信息已替换为占位符
- [ ] `.gitignore` 包含 `.env`、`*.local`
- [ ] README 说明了凭证配置方式

### 7.3 规范性

- [ ] 文件命名使用 `kebab-case`
- [ ] 代码块有语言标注
- [ ] 表格格式正确
- [ ] 禁止操作有明确标注（❌）

---

## 8. 复盘与知识沉淀

每次重大更新或问题修复后，记录复盘文档：

```markdown
# YYYY-MM-DD 复盘

## 关键事件
## 错误与修复
## 成功经验
## 新增错误代码
## 工作流程改进
```

---

*最后更新：2026-05-29*
*适用范围：VIPThink 团队所有 Skill 开发*
