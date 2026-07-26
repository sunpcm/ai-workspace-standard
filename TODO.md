# TODO

AEWS v0.1.0 已发布，当前进入 v0.2 validation and template hardening。
接下来优先用真实仓库稳定人工检查和 canonical role 映射，再实现轻量
validator；不急着加 hooks、MCP、memory runtime 或复杂 CLI。

## P0: 继续开发前先做

Status: Completed on 2026-06-29.

### 1. 补 `CONTRIBUTING.md`

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

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

Status: Completed.

在发布前先确认：

```bash
cd <repo-root>
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

## P3: v0.2 验证与模板加固

### 10. 用 ECC v2.0.0 做大型 reference evaluation

Status: Completed on 2026-07-26.

目标：验证 AEWS 对大型多 harness 仓库的解释力，同时保持 AEWS 与
agent harness 的产品边界。

交付物：

- `examples/reference-evaluations/ecc-v2.0.0.md`
- 本地 `ECC/` checkout 加入 Git ignore

结论：

- adapter 行数只能作为 warning，不能单独决定通过或失败；
- adoption repo 必须允许等价 canonical 文档；
- trust、human promotion 和 supersession 值得进入知识治理讨论；
- hooks、MCP、memory runtime、orchestration 和 installer 仍不属于 AEWS
  core。

### 11. 把 validator 设计收敛为 template/adoption 两种模式

Status: Completed on 2026-07-26.

目标：避免 validator 把 preferred filename 当成唯一合法文档结构。

已完成：

- template mode 可以验证 AEWS 首选路径；
- adoption mode 先解析显式 canonical role mapping；
- Project、Decisions、Handoff、Experiment、Adapter 按角色验证；
- line count 保持 warning；
- exact mapping input 已在第二个真实仓库评估后收敛为可选
  `aews.json`。

证据：

- `docs/validator-design.md`
- `docs/validation-checklist.md`
- `DECISIONS.md`

### 12. 评估一个普通应用仓库

Status: Completed on 2026-07-26.

目标：避免 validator 只适配 AEWS template 和 ECC harness 两个极端。

交付物：

- 一份不复制私有代码或敏感信息的 reference evaluation；
- Project / Decisions / Handoff / Experiment / Adapter role mapping；
- 对 template mode 与 adoption mode failure/warning 边界的验证；
- 对 mapping input 最小格式的建议。

验收标准：

- 只读评估，不要求目标仓库为了通过检查而重命名文档；
- 明确区分缺少 canonical role 与仅使用不同文件名；
- 记录误报、漏报和不适用项；
- 不把目标仓库业务知识复制进 AEWS。

交付结果：

- `examples/reference-evaluations/full-stack-application.md`
- 目标仓库全程只读，未运行依赖、测试、服务或部署命令；
- Project role 需要一个 primary router 加可选 supplements；
- Decisions role 的分散内容属于真实缺失，不是文件名差异；
- 计划文件只有满足新鲜度与 handoff 字段时才能映射为 Handoff；
- 未声明 adapter 时不推断 agent 使用；
- 本地 Markdown 失效引用应成为 validator warning；
- 最小 mapping input 确定为 routing-only `aews.json`。

### 13. 实现第一版只读 validator

Status: Completed on 2026-07-26.

第一版只实现已经通过两类真实仓库验证的机械检查：

- canonical role presence 和显式 mapping；
- `aews.json` primary / supplements / missing / inactive 校验；
- mapped document 本地引用有效性；
- adapter 引用有效性；
- adapter line-count warning；
- 明显重复 durable sentence warning；
- template/adoption mode 不同 failure level；
- 纯文本输出和稳定 exit code。

暂时不要实现：

- 自动文档重写；
- 语义模型或 embedding；
- agent-specific AST/parser；
- hooks、MCP 或常驻服务；
- npm / Python package 发布。

交付结果：

- `scripts/aews_validate.py`
- `docs/validator.md`
- `tests/test_validator.py`
- template-valid、adoption-valid、adoption-warnings、adoption-invalid fixtures
- Python 3.10+ 标准库实现，无第三方依赖；
- template/adoption mode、外置 mapping、稳定 text output 与 exit code；
- mapped path、supplement routing、本地 Markdown 引用、adapter routing、
  line count 和明显重复句检查；
- validator 不生成、不重写目标文件。

验证结果：

- 8 个 `unittest` 全部通过；
- AEWS template mode：0 failures / 0 warnings；
- ECC adoption 回归：0 failures，保留预期 warning；
- 普通全栈应用 adoption 回归：0 failures，自动复现人工评估 warning；
- 两个真实参考仓库均未被修改。

### 14. 增加 evidence-backed adapter compatibility matrix

Status: Completed on 2026-07-26.

目标：不再笼统声称 agent 兼容，而是记录每个 adapter 的加载方式、
验证命令、已知限制和最近验证证据。

该矩阵应描述文档投影兼容性，不复制 ECC 的 runtime parity 模型。

交付结果：

- `docs/adapter-matrix.md` 记录 discovery surface、continuity behavior、
  当前证据和已知限制；
- `docs/cross-agent-continuity.md` 定义 start/checkpoint、证据、新鲜度、
  冲突和并发边界；
- Codex、Claude Code、Cursor、Gemini adapters 路由到相同 Handoff 和任务
  队列角色；
- minimal example 增加第二个 Claude Code projection，证明两个 adapter
  可以共享 canonical state；
- 本机确认 Codex CLI `0.145.0` 和 Claude Code `2.1.218` 可用，未消费模型
  额度运行 runtime-loading 测试；Cursor 与 Gemini CLI 当前不可用；
- ECC Memory Vault 只作为可选、unreviewed handoff transport，不进入 AEWS
  core。
- 当前主要兼容目标明确为 Codex 和 Claude Code；Cursor、Gemini 及未来工具
  保留开放 adapter 接口和参考投影，但暂不投入 runtime 开发与验证。

### 15. 为 Codex 和 Claude Code 增加受控 runtime-loading evidence

Status: In progress on 2026-07-26.

目标：在明确授权模型调用后，用只读临时 fixture 验证两个工具是否真实
加载相同 canonical roles 和当前 next step。

验收标准：

- 记录工具版本、fixture commit、命令形态、观察到的文件、日期和结果；
- prompt 明确禁止修改文件；
- 验证前后 fixture 和 AEWS 工作区保持不变；
- 不把单一版本的成功夸大成所有版本兼容；
- 不保存凭证或原始私有 transcript。

当前结果：

- 新增 `tests/fixtures/runtime-loading/`，静态 validator 为 0 failures / 0
  warnings；
- Codex CLI `0.145.0` 在 read-only、ephemeral、ignore-user-config 条件下
  成功返回仅存在于自动加载 `AGENTS.md` 的 marker，并读取相同 Handoff；
- Codex 探针前后临时 Git commit、状态和四个关键文件 SHA-256 未变化；
- Claude Code 探针在进程启动前被 host approval reviewer 拒绝，未向外部
  服务发送 fixture；需要项目 owner 明确授权把该公开合成 fixture 发送给
  Claude 后才能补证据；
- 证据记录：`docs/runtime-loading-evidence.md`。

## 当前推荐顺序

1. 再选择一个 adoption candidate 使用 validator，观察 warning 稳定性
2. 决定是否增加可复用 adoption mapping template
3. owner 返回后，明确授权 Claude external transfer 并补唯一一次探针
4. 可选：补 GitHub Release 页面说明 `v0.1.0`

## 每次继续开发前的检查命令

```bash
cd <repo-root>
git status --short --branch
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
python3 scripts/aews_validate.py . --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

## 当前不要做

- 不要把 `AGENTS.md` 扩写成完整项目说明；
- 不要新增 hooks / MCP / memory runtime；
- 不要做自动生成器；
- 不要让 canonical standard 绑定 Codex 或 Claude 的专有行为；兼容性实现
  与证据可以优先这两个当前实际使用的工具；
- 不要把个人全局偏好写进公开模板。
