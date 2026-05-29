---
name: skill-uploader
description: "自动化技能上传助手，执行规范性检查、脱敏处理、GitHub上传。当用户需要上传技能到GitHub时立即使用。"
---

# Skill Uploader - 技能上传助手

本 Skill 提供完整的技能上传流程，包括规范性检查、脱敏处理、GitHub 上传等全链路自动化。

## 触发条件

当用户提到以下任何内容时立即使用本 Skill：
- 上传技能
- 检查技能脱敏
- 批量上传
- 发布技能到GitHub
- skill上传

## 前置要求

- GitHub API Token 已配置
- 目标仓库：https://github.com/Nichangcheng0528/Nichagncheng-skill
- 本地技能目录：C:\Users\51773\.trae-cn\skills\

## 上传流程

### Phase 1: 准备阶段
确认上传范围、检查本地技能存在性

### Phase 2: 规范性检查
检查 SKILL.md、_meta.json、README.md 等文件完整性

### Phase 3: 脱敏检查
扫描 API Key、手机号、密码、Token、Cookie 等敏感信息

### Phase 4: 脱敏处理
自动替换为占位符，生成脱敏版本

### Phase 5: 上传到 GitHub
初始化 Git、提交、推送到远程仓库

### Phase 6: 验证与记录
验证上传结果、生成报告

## 使用工具

使用 skill-uploader.py 脚本自动化执行：
- 列出技能：python skill-uploader.py
- 上传单个：python skill-uploader.py <skill-name>
- 批量上传：python skill-uploader.py --batch skill1 skill2

## 分类体系

技能按以下分类体系组织：
- business/: 业务类技能（CRM、销售、数据分析等）
- productivity/: 生产力工具（文档处理、周报生成等）
- audio/: 音频处理（语音转写、录音分析等）
- meta/: 元技能（技能生成、上传、管理等）
- platform/: 平台集成（第三方服务对接等）

## 注意事项

1. 上传前必须执行脱敏检查
2. 确保文件编码为 UTF-8 无 BOM
3. SKILL.md 必须包含完整的 frontmatter
4. 上传后验证 GitHub 仓库状态
