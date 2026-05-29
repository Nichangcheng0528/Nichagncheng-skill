# Nichagncheng-skill

海外业务技能仓库，用于存储、管理和共享自动化技能（Skills）。

## 仓库说明

本仓库存放海外业务团队使用的各类自动化技能，涵盖数据分析、CRM 录音分析、技能生成与管理等领域。所有技能均已脱敏处理，可安全共享。

## 目录结构

```
Nichagncheng-skill/
├── business/                    # 业务类技能
│   └── analytics/              # 数据分析
│       ├── ni-changcheng-knowledge/         # 业务知识库
│       └── overseas-business-analytics/      # 海外业务数据分析
│
├── audio/                       # 音频处理类技能
│   └── recording/               # 录音分析
│       └── vipthink-crm-recording/           # CRM 录音分析（脱敏版）
│
├── meta/                        # 元技能（技能管理工具）
│   └── skill/                   # 技能生成与管理
│       ├── skill-generator/                  # 技能生成器
│       └── skill-uploader/                   # 技能上传助手
│
├── .gitignore                   # Git 忽略规则
└── README.md                    # 本文件
```

## 技能列表

| 技能名称 | 分类 | 版本 | 说明 |
|---------|------|------|------|
| ni-changcheng-knowledge | business/analytics | - | 业务知识库，全局上下文注入 |
| overseas-business-analytics | business/analytics | 1.0.0 | 海外业务数据分析自动化 |
| vipthink-crm-recording | audio/recording | 7.0 | CRM 录音分析（脱敏版） |
| skill-generator | meta/skill | 1.0.0 | 技能生成器 |
| skill-uploader | meta/skill | 1.0.0 | 技能上传助手 |

## 技能包规范

每个技能包包含以下标准文件：

| 文件 | 说明 |
|------|------|
| SKILL.md | 技能定义文件（含 frontmatter 元数据） |
| README.md | 技能说明文档 |
| _meta.json | 技能元数据（名称、版本、分类等） |
| VERSION | 版本号 |
| CHANGELOG.md | 变更记录 |

## 安全说明

- 本仓库为**公开仓库**，所有内容均已脱敏处理
- 真实凭证（CRM 账号、API Key 等）仅存储在本地环境变量中
- 使用前请通过环境变量或 `.env` 文件配置真实凭证
- `.env` 文件已加入 `.gitignore`，不会被提交

## 配置方式

如需使用需要凭证的技能，请创建本地 `.env` 文件（不会上传到 Git）：

```bash
# 示例：CRM 录音分析技能
CRM_USERNAME=你的账号
CRM_PASSWORD=你的密码
DASHSCOPE_API_KEY=你的API Key
```

## 维护者

- [Nichangcheng0528](https://github.com/Nichangcheng0528)

## 更新时间

2026-05-29
