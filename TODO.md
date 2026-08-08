# TODO

AEWS v0.2 validation and template hardening 阶段已完成，v1.0.0 本地发布
材料已经收尾，外部发布交由 owner 手动执行。所有产品与本地 roadmap 任务
已完成；hooks、MCP、memory runtime 或复杂 CLI 继续保持在 core scope
之外。

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

Status: Completed on 2026-07-27.

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
- 已依据 Claude Code `2.1.218 --help` 固化唯一待执行命令：仅开放 `Read`、
  plan permission、project-only settings、无 MCP/浏览器/session persistence、
  结构化输出且预算不超过 USD 1；marker 不出现在 prompt/schema 中；
- 完整参数和 JSON schema 的本地 parser smoke 以 `--help` 退出码 `0` 通过，
  未触发模型调用；
- 已补全六个 fixture 文件的前后 SHA-256 验收条件，增加 checked-in
  `SHA256SUMS` 和回归测试防止 evidence drift；
- owner 明确授权后，仅执行一次 Claude Code `2.1.218` 探针；实际费用约
  USD 0.1006，返回预期 marker、四个 canonical 文件和共享 checkpoint；
- Claude 探针前后临时 commit、clean status、六个 hash 和八文件清单均未
  变化，无 permission denial，无 repo 内 session/result artifact；
- 证据记录：`docs/runtime-loading-evidence.md`。

### 16. 用第三个真实仓库稳定 adoption warning

Status: Completed on 2026-07-26.

目标：验证 experiment-heavy、同时包含 Codex/Claude adapter 且工作区已有
改动的应用仓库，避免 validator 只适配干净或文档结构简单的目标。

交付结果：

- 全程使用外置 mapping，只读评估目标仓库；
- 评估前后 `git status --porcelain=v1 -uall` digest 一致；
- 首次运行发现 25 个 generated Markdown artifact basename 误报；
- 收紧 inline-code reference 规则并增加 regression coverage；
- 最终结果为 0 failures / 8 个可解释 warning；
- 结论记录在
  `examples/reference-evaluations/ai-experiment-service.md`。

### 17. 发布可复用 adoption mapping template

Status: Completed on 2026-07-26.

目标：基于三类真实仓库已经稳定的共同字段，提供 routing-only 示例，
不新增未经证据支持的 schema 字段或生成器。

交付结果：

- 新增 `templates/adoption/aews.example.json` 和使用边界说明；
- 同时覆盖 Project primary/supplements、Decisions primary、Handoff 和
  Experiment inactive、Codex/Claude adapter 声明；
- 明确 `missing` 与 `inactive`、checked-in 与外置只读 mapping 的区别；
- 增加测试，从发布模板构造临时目标并通过真实 validator contract；
- 不新增 schema 字段、生成器、运行时状态或工具私有知识。

### 18. 收口 v0.2.0 release readiness

Status: Completed on 2026-07-26.

交付结果：

- 新增 `CHANGELOG.md`，区分已发布 `v0.1.0` 与未发布的 v0.2 candidate；
- 新增 `docs/releases/v0.2.0-readiness.md`，记录本地检查、已知限制和发布
  边界；
- v0.2.0 本地 release candidate 可以交由 owner 审核、push、tag 和发布；
- 当时 v1.0 由 Claude Code runtime-loading evidence 阻塞；该项已在 #15
  完成，并由 #19 重新审计；
- 本轮不执行 push、tag、GitHub Release 或任何外部发布操作。

### 19. 完成 v1.0.0 release readiness

Status: Completed on 2026-07-27.

交付结果：

- Codex 与 Claude Code 均有同一合成 checkpoint 的受控 runtime-loading
  证据；
- 补充 v1.x 兼容性、major/minor/patch 和 mapping contract version 规则；
- 新增 `docs/releases/v1.0.0-readiness.md`，逐项映射 v1 exit criteria 到
  权威证据；
- 因 v0.2.0 从未发布且 v1 条件已全部满足，保留 v0.2 readiness 作为 phase
  evidence，下一本地 candidate 直接提升为 v1.0.0；
- 不执行 push、tag、changelog dating 或 release publication。

### 20. 准备 v1.0.0 正式发布

Status: Local preparation completed on 2026-07-27; external publication handed
to owner.

交付目标：

- README 提供新 repo、已有 repo 和 Codex/Claude 日常接力使用指南；
- README 最小 Quick Start 已转为回归测试，在 Handoff inactive 时保持
  0 failures / 0 warnings；
- `CHANGELOG.md` 固化带日期的 `1.0.0` 条目；
- `docs/releases/v1.0.0.md` 提供可直接用于 GitHub Release 的发布说明；
- release commit 通过完整 validator、测试、hash 和隐私检查；
- 提供 annotated `v1.0.0` tag、push 和 GitHub Release 的手动命令；
- agent 不执行任何外部发布动作；owner 发布后再更新实际远端状态。

### 21. 定义跨 Agent 多服务部署证据协议

Status: Pending after v1.0.0 publication.

目标：当 Codex、Claude Code 或人工分别部署多个服务时，让任一后续 Agent
可以依据共享、可验证的 deployment receipts 汇总全部部署，而不需要读取或
同步其他 Agent 的原始聊天记录。

问题场景：

- 例如 Codex 部署 service A、service B，Claude Code 部署 service C；
- 三次会话彼此独立，默认不能互读 vendor transcript；
- 最终汇总必须回答每个服务部署了什么版本、部署到哪个环境、是否成功、
  如何验证、有哪些风险以及如何回滚；
- 聊天中的计划、推断或“已经完成”声明不能作为部署成功证据。

建议交付物：

- `templates/deployment/DEPLOYMENT.md`：单次部署 receipt 的最小模板；
- `docs/deployment-evidence.md`：记录生命周期、信任边界、单 repo 与多 repo
  聚合方式；
- `examples/multi-service-deployment/`：至少包含两次 Codex 部署、一次
  Claude Code 部署和一个跨三次部署的汇总示例；
- README / adoption guide 中的可选 operations profile 入口；
- 在人工格式稳定后，再评估由 CI/CD 生成 receipt 或索引的轻量自动化。

每份 deployment receipt 至少记录：

- service、environment、部署发起者或 harness；
- source commit、image/artifact digest；
- deployment command、CI/CD run 或外部任务链接；
- started/finished timestamp；
- result 和实际运行版本；
- health/smoke verification 及其证据；
- known risks、rollback target 和 rollback verification；
- receipt 的 freshness / supersession 条件。

权威性规则：

- Git commit、不可变 artifact/image digest、CI/CD 结果和运行环境健康检查
  优先于 Agent prose；
- `HANDOFF.md` 只链接最新部署 checkpoint，不保存累积 transcript；
- `TODO.md` 或外部任务系统保存服务级计划与完成状态；
- receipts 是 operations evidence，不新增 AEWS core canonical role；
- 单 repo 可放在 `operations/deployments/`；多 repo 应使用 workspace/ops
  repo 或已有部署平台作为聚合源，并由各服务 repo 链接过去；
- 不记录 token、secret、完整命令输出或可能泄露环境配置的原始日志。

验收标准：

- Codex 与 Claude Code 都能从同一组 receipts 得到一致的三服务部署摘要；
- 汇总不读取、导入或依赖任何 vendor chat transcript；
- 每个“成功”结论都能追溯到 commit/digest、部署运行和健康验证证据；
- 缺少证据、部署失败、部分成功和已回滚状态不会被误报为成功；
- 并发部署不会依赖多个 Agent 持续重写同一个状态文件；
- 不引入 hooks、MCP、memory runtime、常驻服务或 Agent orchestration；
- 模板和示例通过 validator，且明确这是一项可选 operations profile。

## P4: v1.0.0 之后的候选

### 22. 增加诊断产出物模板与证据校验

Status: Pending.

目标：把“先检索已有材料再做代码推演”从只能被读到的软约束，变成可机械
校验的产出物要求，降低无证据根因排序对读者的误导。

背景证据（来自一次真实复盘，不复制目标仓库业务细节）：

- 两个 Agent 先后只做代码推演，未检索仓库内已存在的事故文档、决策记录
  和 `git log`，也未确认问题是否已有在飞的修复；
- 被标注为“最可能”的根因没有任何证据支撑，且与真实根因相反；
- 因两个语义相近的文档目录，两个 Agent 先后检索错同一个目录。

建议路径：

```text
templates/diagnosis/DIAGNOSIS.md
docs/diagnosis-evidence.md
```

该模板是 Experiment scope 的特化，不新增 canonical knowledge role。

必填段：

- 检索记录：已搜索的路径、匹配模式、`git log` 范围、命中与未命中；
- 候选根因：每条必须带证据字段，取值为 `路径:行号`、commit、日志路径，
  或显式的“无证据 — 仅代码推演”；
- 排序约束：存在“仅推演”候选时，禁止使用“最可能”一类置信度措辞；
- 验证步骤：可执行命令加可证伪的预期结果。

validator 增量检查（保持只读、无第三方依赖）：

- 诊断文档缺少四个必填段之一 → warning；
- 出现置信度措辞但同段落无证据引用 → warning；
- 证据字段引用的本地路径不存在 → 复用现有引用有效性检查。

验收标准：

- 模板不绑定语言、技术栈、厂商或具体故障类型；
- 不新增 canonical role，仅作为 Experiment 特化；
- 检查保持 warning 级别，与 adapter line count 的处理一致；
- 明确记录该模板防不住什么：它不能阻止填写虚假证据，也不能纠正模型在
  被质疑时的立场漂移；
- 至少一个 example 展示“无证据 — 仅代码推演”的正确写法。

### 23. 增加 GitHub Copilot adapter（primary target）

Status: Completed on 2026-08-08.

原计划按 extension reference 加入。owner 说明 Copilot 与 Codex、Claude Code
同为日常主力工具后，改按 primary target 加入。2026-07-26 的优先级决策本身
允许在出现真实使用时提升，因此这是执行既有策略，不是放宽证据要求。

交付结果：

- `adapters/copilot/.github/copilot-instructions.md` 提供投影模板；
- 本仓库新增根 `.github/copilot-instructions.md`，因为 Copilot 的 IDE 侧
  不读取 `AGENTS.md`，没有这个文件时 owner 在本仓库用 Copilot 拿不到路由；
- `scripts/aews_validate.py` 增加 `ADAPTER_FILENAME_TOOLS` 映射，同时发现
  仓库根和 `adapters/` 下的 copilot instructions；
- `standard/adapters.md` 与 `docs/adapter-matrix.md` 增加对应行、最小投影和
  验证命令；
- `DECISIONS.md` 记录提升决策及其证据边界；
- 测试增加 copilot 双位置发现断言，README Quick Start 回归同步覆盖 copilot。

证据等级（不得含糊）：

- Copilot 为 primary priority，但只有 static projection 加 validator pass；
- 只有 Codex 和 Claude Code 具备受控 runtime-loading 证据；
- Copilot 的 IDE 侧没有与 `codex`、`claude` 对等的 headless 只读调用方式，
  受控探针需要人工编辑器会话，尚未执行。

范围限制（已执行）：

- 只投影 `.github/copilot-instructions.md`；
- 未投影 `.github/instructions/*.instructions.md` 的 path-scoped 规则。

版本判定：

- 按 `docs/versioning.md`，新增可选 adapter 与 validator discovery 属于
  backward-compatible，定为 `1.1.0`；
- 判定规则已记入 `DECISIONS.md`，后续新增 adapter 沿用同一路径；
- `1.1.0` 的 release notes 与 readiness 记录仍属 owner 控制的发布准备工作，
  本项不代为执行。

### 24. 落地 Workspace scope 的多仓库形态

Status: Pending. 需要先完成一次真实工作区评估。

目标：`standard/scopes.md` 已定义 Workspace scope，但目前没有任何落地
产物——没有 workspace 级模板，`aews.json` 只有 template 与 adoption 两种
单仓库模式，validator 也要求全部路径位于单个 target 内。

真实场景（第四类评估目标）：

- 工作区根并列多个独立部署、各自持有 `.git` 的子项目；
- 工作区根本身不是 git 仓库，共享规则文件无法随仓库分发给协作者；
- 跨项目文档与项目内文档分处两个语义相近的目录，导致检索错目录。

按既有方法论推进，先评估再收敛 schema：

1. 完成一次只读工作区评估，记录 role 映射、失败与误报；
2. 再决定 `aews.json` 是否增加 workspace mode 及其最小字段；
3. 最后才考虑 validator 的多 target 路径解析。

需要回答的问题：

- workspace 级 role 映射与成员仓库 role 映射的边界；
- 共享规则的分发形态，以及 workspace meta-repo 与各仓库薄投影的关系；
- validator 是否允许在已声明的成员边界内解析跨仓库路径；
- Workspace scope 是否需要独立 canonical 文档，还是复用现有 role。

验收标准：

- 评估全程只读，不要求目标工作区重命名或移动文档；
- 不引入 orchestration、hooks、常驻服务或 agent 间实时协调；
- 若评估结论是现有 adoption mode 已经够用，允许不新增 workspace mode，
  并把该结论记入 `DECISIONS.md`。

### 25. 评估 Handoff 新鲜度检查（先决策，后实现）

Status: Pending decision.

目标：`docs/cross-agent-continuity.md` 已定义 staleness 规则，但 validator
目前只做文件系统层面的只读检查，无法验证 Handoff 声明的 commit 是否真实
存在、是否仍是 HEAD 的祖先。

先决策的问题：

- validator 是否允许调用只读 `git` 命令；这会改变当前“无第三方依赖、纯
  文件系统”的实现前提；
- 若不允许，是否只做不依赖 git 的弱检查，例如必填字段是否为空、时间戳
  格式是否合法。

决策明确后再实现。不要为了增加检查项而扩大 validator 的运行前提。

## 当前推荐顺序

1. owner 检查并 push 本地 release-preparation commit
2. owner 创建和推送 `v1.0.0` annotated tag
3. owner 发布 GitHub Release 并更新发布后状态
4. #22 诊断模板与证据校验：独立价值最高，不依赖外部发布
5. #24 Workspace scope：需先完成一次真实工作区评估
6. #21 与 #25 按需评估，不阻塞上述任何一项

已完成 #23（Copilot primary adapter），其 runtime 探针留待人工编辑器会话，
不阻塞上述任何一项。

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
