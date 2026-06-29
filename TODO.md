# TODO

AEWS 当前处于 v0.1 architecture-first 阶段。接下来优先补齐可维护性和验证闭环，不急着加脚本、hooks、MCP、memory runtime 或复杂 CLI。

## P0: 继续开发前先做

### 1. 补 `CONTRIBUTING.md`

目标：让后续贡献不破坏 AEWS 的核心边界。

交付物：

- `CONTRIBUTING.md`

内容应覆盖：

- 先读哪些文件；
- 如何判断 Scope；
- 如何更新 Decision / Handoff；
- 什么内容不能放进 adapter；
- 提交前如何跑 `docs/validation-checklist.md`。

验收标准：

- 不引入语言栈、厂商或工具假设；
- 明确禁止把 durable knowledge 复制进 `AGENTS.md` / `CLAUDE.md` / Cursor rules / `GEMINI.md`；
- 能被新贡献者在 5 分钟内读完。

### 2. 增加 oversized `AGENTS.md` 迁移示例

目标：证明 AEWS 的价值不是“新增更多文件”，而是把大上下文拆成 canonical docs + thin adapter。

建议路径：

```text
examples/migrations/oversized-agents/
```

交付物：

```text
before/AGENTS.md
after/PROJECT.md
after/DECISIONS.md
after/HANDOFF.md
after/AGENTS.md
README.md
```

验收标准：

- `before/AGENTS.md` 展示典型反模式：架构、命令、决策、任务状态混在一起；
- `after/AGENTS.md` 控制在 30 行以内；
- `README.md` 解释每段内容迁移到哪里，以及为什么。

### 3. 用 validation checklist 自检 minimal example

目标：让 `docs/validation-checklist.md` 不只是文档，而是能真实约束示例质量。

交付物：

- `examples/minimal-repo/VALIDATION.md`

内容应包含：

- 对 `docs/validation-checklist.md` 每一大项的通过/不适用说明；
- 发现的问题；
- 是否需要更新模板或标准。

验收标准：

- 不夸大 minimal example 的覆盖范围；
- 明确记录“不适用”的原因；
- 如果发现 checklist 不好用，优先修改 checklist，而不是绕过。

## P1: v0.1 质量加固

### 4. 补 adoption guide

目标：让用户知道如何把现有 repo 迁移到 AEWS。

建议路径：

```text
docs/adoption-guide.md
```

建议结构：

- 适合采用 AEWS 的场景；
- 不适合采用 AEWS 的场景；
- 从单一 `AGENTS.md` 迁移；
- 从多 agent 配置迁移；
- 最小落地路径；
- 常见错误。

验收标准：

- 先推荐最小采用，不推荐一步到位；
- 明确说明 AEWS 不替代项目文档、CI、测试和运行手册；
- 不把 ECC 的 harness 能力包装成 AEWS v0.1 范围。

### 5. 补 versioning policy

目标：避免标准文件变动后没有兼容性说明。

建议路径：

```text
docs/versioning.md
```

需要回答：

- v0.x 什么算 breaking change；
- adapter 文件变化是否算 breaking；
- template 字段变化如何迁移；
- examples 是否跟随标准版本。

验收标准：

- 能指导未来打 `v0.1.0`；
- 不引入复杂发布流程；
- 明确 v0.1 仍允许调整结构，但要记录决策。

### 6. 增加 template review checklist

目标：防止 templates 变成完整框架 scaffold。

建议路径：

```text
templates/README.md
```

内容应说明：

- 每个模板的用途；
- 什么时候不要使用模板；
- 如何保持模板最小；
- 修改模板时需要同步哪些文档。

验收标准：

- 不新增模板字段，除非能解释生命周期或 scope 价值；
- 不绑定语言、包管理器、云厂商或 AI 厂商。

## P2: 等 v0.1 稳定后再考虑

### 7. 设计轻量 validator，而不是马上实现

目标：先定义自动检查范围，再决定是否写脚本。

建议先写：

```text
docs/validator-design.md
```

只讨论：

- 检查 adapter 行数；
- 检查 canonical 文件是否存在；
- 检查明显重复句子；
- 检查 forbidden runtime features 是否被提前引入。

暂时不要做：

- 复杂 AST；
- agent-specific parser；
- 自动重写文档；
- npm / Python 包发布。

### 8. 准备 v0.1.0 release checklist

建议路径：

```text
docs/release-checklist.md
```

内容应包括：

- Git 状态；
- License；
- README；
- Decisions；
- Handoff；
- minimal example；
- migration example；
- validation checklist 结果。

### 9. 再决定是否创建 GitHub remote

在发布前先确认：

```bash
cd /Users/sunpcm/code/ai-workspace-standard
git status --short --branch
git log --oneline --decorate -5
```

如果要创建远端，再执行类似命令：

```bash
gh repo create ai-workspace-standard --public --source . --remote origin --push
```

风险说明：

- `--public` 会公开仓库；
- 推送前必须确认没有私人偏好、路径、token、内部项目细节。

## 当前推荐顺序

1. `CONTRIBUTING.md`
2. `examples/migrations/oversized-agents/`
3. `examples/minimal-repo/VALIDATION.md`
4. `docs/adoption-guide.md`
5. `docs/versioning.md`
6. `templates/README.md`
7. `docs/validator-design.md`
8. `docs/release-checklist.md`

## 每次继续开发前的检查命令

```bash
cd /Users/sunpcm/code/ai-workspace-standard
git status --short --branch
find . -maxdepth 4 -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
```

## 当前不要做

- 不要把 `AGENTS.md` 扩写成完整项目说明；
- 不要新增 hooks / MCP / memory runtime；
- 不要做自动生成器；
- 不要绑定 Codex、Claude、Cursor 或 Gemini 任一厂商；
- 不要把个人全局偏好写进公开模板。
