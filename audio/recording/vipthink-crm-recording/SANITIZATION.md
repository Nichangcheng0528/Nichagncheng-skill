# 安全与脱敏规范

> 本文档定义了 Skill 开发和上传过程中的安全规范，确保敏感信息不会泄露到代码仓库。

---

## 1. 为什么需要脱敏？

- **保护账号安全**：CRM 账号、API Key 等凭证一旦泄露，可能被恶意使用
- **合规要求**：公司数据安全规范要求代码仓库中不得包含明文凭证
- **团队协作安全**：仓库对团队成员可见，脱敏版本可安全分享

---

## 2. 必须脱敏的内容

### 2.1 账号密码类

| 类型 | 示例 | 脱敏后 |
|------|------|--------|
| CRM 登录账号 | `18501099917` | `<YOUR_CRM_USERNAME>` |
| CRM 登录密码 | `Ncc19930528@` | `<YOUR_CRM_PASSWORD>` |
| 邮箱账号密码 | `user@vipthink.cn:pass123` | `<EMAIL>:<PASSWORD>` |
| 数据库连接串 | `mongodb://user:pass@host` | `mongodb://<USER>:<PASSWORD>@host` |

### 2.2 API Key / Token 类

| 类型 | 示例 | 脱敏后 |
|------|------|--------|
| DashScope API Key | `sk-99f9364af58c49d5b927f43dc08e2e5c` | `<YOUR_DASHSCOPE_API_KEY>` |
| 通用 API Key | `sk-xxxxxxxxxxxx` | `<YOUR_API_KEY>` |
| Bearer Token | `Bearer eyJhbGci...` | `Bearer <TOKEN>` |
| Access Token | `access_token = "abc123..."` | `access_token = <ACCESS_TOKEN>` |
| Secret Key | `secret_key = "xyz789..."` | `secret_key = <SECRET_KEY>` |

### 2.3 个人信息类

| 类型 | 示例 | 脱敏后 |
|------|------|--------|
| 员工手机号（作为账号） | `13800138000` | `<PHONE_NUMBER>` |
| 员工个人微信 | `wxid_abc123` | `<WECHAT_ID>` |

---

## 3. 不需要脱敏的内容

以下内容属于业务标识，不是凭证，**不需要脱敏**：

- 飞书文档 token（`doc_token`、`board_token`）— 业务标识
- CRM 系统 URL（`https://ecc.vipthink.cn`）— 公开地址
- 员工姓名（用于组织架构说明）— 公开信息
- 团队名称、组别名称 — 公开信息
- API 端点 URL — 公开地址

---

## 4. 脱敏工具使用

### 4.1 自动化脱敏工具

我们使用 `skill-sanitizer.py` 自动生成脱敏版本：

```bash
# 生成所有 skills 的脱敏版本
python skill-sanitizer.py

# 只生成指定 skill 的脱敏版本
python skill-sanitizer.py vipthink-crm-recording
```

### 4.2 脱敏配置

脱敏规则定义在 `skill-sanitizer-config.json` 中，支持：

| 配置项 | 说明 |
|--------|------|
| `match` | 要匹配的字符串或正则表达式 |
| `replace` | 替换后的占位符 |
| `regex` | 是否为正则表达式（默认 false） |
| `skills` | 适用的 skill 列表（`*` 表示所有） |

### 4.3 添加新的脱敏规则

```json
{
  "name": "规则名称",
  "description": "规则说明",
  "match": "要匹配的内容",
  "replace": "<PLACEHOLDER>",
  "regex": true,
  "skills": ["*"]
}
```

---

## 5. 上传流程规范

### 5.1 标准上传流程

```
1. 在 skills/ 目录正常开发和测试（包含真实凭证）
         ↓
2. 运行脱敏工具生成 skills-upload/ 目录
         ↓
3. 验证脱敏效果（检查是否还有敏感信息残留）
         ↓
4. 从 skills-upload/ 目录推送到 GitHub
         ↓
5. 确认推送成功
```

### 5.2 上传前检查清单

- [ ] 所有真实账号已替换为 `<YOUR_XXX>` 占位符
- [ ] 所有真实密码已替换为 `<YOUR_XXX>` 占位符
- [ ] 所有 API Key 已替换为 `<YOUR_XXX>` 占位符
- [ ] `.env` 文件已添加到 `.gitignore`
- [ ] 脱敏版本中包含 `.sanitized` 标记文件
- [ ] README 中说明了凭证配置方式

### 5.3 验证命令

```bash
# 检查是否还有敏感信息残留
grep -r "18501099917\|Ncc19930528@\|sk-99f9364" skills-upload/
# 应该没有任何输出
```

---

## 6. 日常开发规范

### 6.1 凭证管理原则

| 原则 | 说明 |
|------|------|
| **环境变量优先** | 通过 `os.environ.get()` 读取凭证，不硬编码 |
| **.gitignore 必配** | `.env`、`*.local`、`credentials.json` 必须排除 |
| **占位符清晰** | 使用 `<YOUR_XXX>` 格式，让使用者明确需要配置什么 |
| **文档说明** | README 中必须说明凭证配置方式 |

### 6.2 推荐的凭证读取方式

```python
import os

# 推荐方式：从环境变量读取
CRM_USERNAME = os.environ.get("CRM_USERNAME", "")
CRM_PASSWORD = os.environ.get("CRM_PASSWORD", "")
DASHSCOPE_API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")

# 不推荐：硬编码
# CRM_USERNAME = "18501099917"  # ❌ 禁止
```

---

## 7. 违规处理

如果发现代码仓库中存在明文敏感信息：

1. **立即处理**：在最近的提交中移除敏感信息
2. **更换凭证**：如果信息已推送，立即更换对应的账号密码或 API Key
3. **复盘改进**：检查脱敏工具规则是否完善，补充遗漏的规则

---

*最后更新：2026-05-29*
