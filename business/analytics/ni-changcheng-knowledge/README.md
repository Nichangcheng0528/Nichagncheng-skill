# Ni Changcheng K12 Overseas Education Knowledge Base

## Overview

This skill provides global context injection for Trae conversations. When triggered by business keywords, it automatically loads the Ni Changcheng knowledge base and applies the appropriate writing style.

## Trigger Keywords

- **High Priority**: 复盘, 月报, GMV, leads, 转化率, 达成率, ASP, CC, 港澳, 台湾, 薪酬, 绩效, PIP
- **Medium Priority**: 话术, 异议, 签单, 新人, 培训, 离职, 产能

## Knowledge Sources

| Source | Path | Priority |
|--------|------|----------|
| Context Manual | `d:\Trae工作内容\BI数据分析\00_上下文衔接手册.md` | Always |
| Style Manual | `d:\Trae工作内容\BI数据分析\倪常程风格手册.md` | On demand |
| Knowledge Graph | `d:\Trae工作内容\BI数据分析\K12海外教育知识图谱与全局适配手册.md` | On demand |
| Knowledge Folder | `C:\Users\51773\Desktop\knowledge\` | On demand |

## Style Rules

- Data-driven: every claim backed by numbers
- Direct: no hedging, state conclusions first
- Quantified: precise to 2 decimal places
- Reward/punishment clear: explicit incentives and consequences

## File Structure

```
ni-changcheng-knowledge/
├── SKILL.md              # Skill definition
├── VERSION               # Version number
├── CHANGELOG.md          # Change history
├── README.md             # This file
├── agents/
│   └── openai.yaml       # Agent interface config
└── scripts/
    └── validate_skill_package.py  # Package validator
```
