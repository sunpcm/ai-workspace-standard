# DECISIONS

记录应当影响未来 AEWS 工作的已接受决策。

## 决策

### 2026-06-29：把 AEWS 建成一个标准，而不是 ECC 的克隆

Status: Accepted

Scope: Workspace

背景：ECC 是一个覆盖 agents、skills、hooks、commands、MCP、安全和 memory 的
广义 agent harness。

决策：AEWS v0.1 专注于工作区知识结构、范围、生命周期、模板和适配器投影。

后果：运行时特性被推迟。在规范模型稳定之前，本仓库保持文档优先。

Evidence: `docs/architecture.md`, `docs/roadmap.md`

### 2026-06-29：以 Scope First 作为首要的放置规则

Status: Accepted

Scope: Workspace

背景：大型代理指令文件往往会积累混杂的关注点和过期上下文。

决策：AEWS 在选择文档或适配器之前，先把信息归类为 Global、Workspace、Repo
或 Experiment。

后果：新文档和新模板必须声明其预期范围。

Evidence: `docs/scope-first.md`, `standard/scopes.md`

### 2026-06-29：保持适配器轻量

Status: Accepted

Scope: Workspace

背景：Codex、Claude Code、Cursor、Gemini CLI 以及未来的代理需要不同的文件
格式，但它们不应各自持有独立的知识副本。

决策：适配器文件只包含读取顺序和工具专属行为。

后果：持久的项目事实属于规范文档，而不是适配器文件。

Evidence: `standard/adapters.md`, `docs/adapter-matrix.md`

### 2026-06-29：初始开源标准采用 MIT 许可证

Status: Accepted

Scope: Repo

背景：AEWS 的设计意图是被克隆、改编，并作为模板在不同团队与工具间使用。

决策：本仓库使用 MIT License。

后果：采用门槛保持很低，但不提供担保、也不承担责任。

Evidence: `LICENSE`

### 2026-06-29：先有人工验证检查表，再谈自动化

Status: Accepted

Scope: Repo

背景：v0.1 应该先用人工方式验证这个标准，然后再加入脚本或自动生成的行为。

决策：AEWS 使用 `docs/validation-checklist.md` 作为文档、模板、示例和适配器
变更的验收门槛。

后果：在检查表通过真实使用稳定下来之前，自动化被推迟。v0.2 的首个证据门槛已
于 2026-07-26 达成；此后只有已被验证的机械检查可以推进。

Evidence: `docs/validation-checklist.md`, `docs/roadmap.md`

### 2026-07-26：先校验规范角色，再校验首选文件名

Status: Accepted

Scope: Workspace

背景：ECC v2.0.0 的参考评估显示，一个既有仓库完全可能在不同文件名下持有受
治理的项目事实、决策、工作状态和适配器。只看文件名的验证器会报出本可避免的
warning，并可能在采用过程中鼓励产生重复文档。

决策：v0.2 的验证器设计区分 AEWS template 模式与既有仓库的 adoption 模式。
template 模式可以要求 AEWS 的首选路径。adoption 模式必须校验显式映射的规范
角色，并在应用文件名相关检查之前，先报告它所使用的映射。

后果：AEWS 保留首选文件名，但不把它们变成普适要求。映射输入格式被刻意推迟到
人工评估过一个普通应用仓库之后，现记录在下一条决策中。

Evidence: `docs/validator-design.md`,
`examples/reference-evaluations/ecc-v2.0.0.md`

### 2026-07-26：采用映射使用仅做路由的 JSON 清单

Status: Accepted

Scope: Workspace

背景：那个普通全栈应用的评估发现，持久的项目知识被拆分在一个根级路由文档、
一份架构概览和若干组件运行手册之中。评估还发现 Decisions 与 Handoff 角色是
真实缺失的。只用 CLI 参数无法提供可重复的 CI 输入，而散文式的约定又难以被
机械校验。

决策：adoption 模式接受一个可选的 `aews.json` 清单，或指向等价 JSON 文件的
显式路径。它为每个角色映射一个 primary 文档和可选的 supplements，映射显式的
`missing` 状态或被允许的 `inactive` 状态，以及已声明的适配器路径。

后果：既有仓库无需重命名或复制文档就能被校验。该清单是一层路由投影，绝不能
持有项目事实、决策、命令或工作状态。验证器不得生成或重写它。

Evidence: `docs/validator-design.md`, `standard/documents.md`,
`templates/adoption/aews.example.json`,
`examples/reference-evaluations/full-stack-application.md`

### 2026-07-26：第一版验证器保持无依赖且只读

Status: Accepted

Scope: Repo

背景：ECC 与普通应用这两次评估，稳定下来一小组机械检查。在这些能力尚无证据
之前就引入包管理、Markdown 解析器、语义模型或重写行为，会抬高采用成本和信任
成本。

决策：第一版验证器是一个 Python 3.10+ 标准库脚本。它读取目标仓库和可选的 JSON
映射，产出文本结论和稳定的退出码，且绝不修改目标。测试使用 `unittest` 和检入
的 fixture，不引入第三方依赖。

后果：实现保持可审阅、可移植，但本地文档解析刻意保守。安装时生成的路径和语义
层面的生命周期问题，仍作为需人工评审的 warning，而不是隐藏的启发式判断。

Evidence: `scripts/aews_validate.py`, `tests/test_validator.py`,
`docs/validator.md`

### 2026-07-26：把跨代理连续性定义为可选的文档协议

Status: Accepted

Scope: Workspace

背景：Codex 和 Claude Code 可以读取相同的规范项目文档，但仅有共享文档并不能
证明另一个代理改了什么，也不能防止并发编辑。ECC 展示了有价值的显式交接与
memory 传输，同时也印证了会话捕获、MCP、在线状态和编排属于 harness 运行时的
关注点。

决策：AEWS 定义一个可选的跨代理连续性 profile。所有参与的代理读取相同的
Project、Decisions、Handoff 和任务队列角色；Git 与已验证的工件提供实现证据；
检查点更新取代转录式的活动日志。运行时 memory 可以传输未经评审的交接，但它
位于 AEWS 核心之外，且不会自动成为受治理的事实。

后果：仓库无需引入运行时，就能支持从 Codex 到 Claude 的续接。AEWS 不承诺实时
感知、文件锁定或自动的转录同步。并发的代理应使用独立分支或 worktree，运行时
专属的自动化仍属于可选集成。

Evidence: `docs/cross-agent-continuity.md`, `docs/adapter-matrix.md`,
`examples/reference-evaluations/ecc-v2.0.0.md`

### 2026-07-26：优先保障 Codex 与 Claude Code 的兼容性证据

Status: Accepted

Scope: Workspace

背景：项目 owner 当前使用 Codex 和 Claude Code。把每一个可能的代理工具都当作
同等的实现目标，会把验证精力分散到并不属于活跃工作流的工具上，也会让兼容性
表述难以维持。

决策：在当前 AEWS 路线图中，Codex 和 Claude Code 是主要兼容目标。规范角色
模型、适配器规则和采用映射保持与厂商无关，以便 Cursor、Gemini CLI 及未来工具
自行添加轻量适配器。既有的非主要投影可以作为参考示例保留，但除非真实使用或
新证据改变优先级，AEWS 不承诺为它们做开发或运行时测试。

后果：运行时加载测试、跨代理连续性示例和近期的兼容性文档将聚焦 Codex 和
Claude Code。非主要的适配器条目必须标注为扩展参考，而不是等同的支持承诺。
规范标准不得沾染 Codex 或 Claude 的专有知识。

Evidence: `PROJECT.md`, `docs/adapter-matrix.md`, `docs/roadmap.md`

### 2026-07-26：不从任意裸 Markdown 文件名推断文档链接

Status: Accepted

Scope: Repo

背景：第三次采用评估出现了二十五条误报 warning，原因是那个应用仓库在行内代码
中记录了 `summary.md`、`batch_summary.md` 这类生成产物。它们的 `.md` 后缀并不
意味着它们是检入仓库的文档。

决策：无依赖验证器继续检查常规 Markdown 链接、带目录限定的行内路径、显式相对
路径，以及已知的规范根文件名。它不再把其他所有裸的行内代码 `.md` 文件名当作
仓库链接。

后果：生成的报告目录不再主导 adoption 输出。若作者确实想用一个裸的自定义文件名
引用另一份检入文档，应使用常规 Markdown 链接或显式相对路径。

Evidence: `scripts/aews_validate.py`, `tests/fixtures/adoption-warnings/README.md`,
`examples/reference-evaluations/ai-experiment-service.md`

### 2026-07-27：把已完成的验证阶段直接提升为 v1.0 候选版

Status: Accepted

Scope: Repo

背景：v0.2 验证阶段产出了三份真实仓库评估、一份稳定的映射契约、一个经过测试
的只读验证器、一条迁移路径，以及两个主要工具的版本范围运行时加载证据。当时没有
发布 v0.2 标签，因此不存在依赖中间版本的外部 v0.2 消费者。所有文档化的 v1.0
退出标准此时均已具备证据。

决策：保留 v0.2.0 的 readiness 记录作为阶段证据，但把下一个本地候选版直接定为
`v1.0.0`，而不发布中间的 v0.2.0 标签。v1 稳定表面包括范围模型、规范角色、
轻量适配器契约、采用映射版本 1、只读验证器和可选的检查点连续性协议。

后果：未来对这一稳定表面的破坏性变更，需要走 `docs/versioning.md` 中的主版本
流程。推送、打标签、changelog 日期化和发布仍由 owner 控制。不得把缺少 v0.2
标签表述为缺失的迁移依赖，因为 v0.2 从来不是已发布的兼容性基线。

Evidence: `docs/releases/v0.2.0-readiness.md`,
`docs/releases/v1.0.0-readiness.md`, `docs/runtime-loading-evidence.md`,
`docs/roadmap.md`

### 2026-08-08：新增 Secondary 层级并把 GitHub Copilot 放入其中

Status: Accepted

Scope: Repo

背景：2026-07-26 的决策把 Codex 和 Claude Code 定为主要兼容目标，因为它们是
owner 当时的活跃工具，同时该决策允许在某个工具产生真实使用后将其提升。owner
现在每天使用 GitHub Copilot，但它扮演的是辅助角色而非主力。Copilot coding
agent 能读取根 `AGENTS.md`，而 IDE 侧读取的是 `.github/copilot-instructions.md`，
因此既有的 Codex 投影覆盖不到日常的编辑器使用。

原有的两层模型无法表达这种状态。把 Copilot 称为 Primary 会暗示它具备并不存在
的运行时加载证据；称之为 extension reference 又低估了真实的维护投入。

决策：新增第三层。Primary 指被积极使用的主力工具，具备维护中的适配器、验证器
发现逻辑，以及受控的运行时加载证据；Codex 和 Claude Code 留在这一层。Secondary
指同等的维护承诺，但不作运行时证据声明；GitHub Copilot 归入这一层，配一份轻量
的 `.github/copilot-instructions.md` 投影和 template 模式发现逻辑。Extension
reference 保持不变。

只投影仓库级的 instructions 文件。路径限定的 `.github/instructions/*.instructions.md`
规则留给采用方仓库，因为激活 glob 属于编辑器行为，而不是规范知识路由。

后果：每一层现在都自述其保证，因此运行时声明不会跨层泄漏，也不再需要用逐工具
的附注去修正层级标签。要把 Copilot 提升为 Primary，需要一次人工编辑器探针，
因为它的 IDE 侧没有与 `codex` 或 `claude` 对等的 headless 只读调用方式。最小
示例继续只演示两个 Primary 工具，这在新模型下依然自洽。

Evidence: `adapters/copilot/.github/copilot-instructions.md`,
`docs/adapter-matrix.md`, `standard/adapters.md`, `scripts/aews_validate.py`

### 2026-08-08：把适配器发现逻辑的新增归类为 minor 版本

Status: Accepted

Scope: Repo

背景：新增 GitHub Copilot 需要在 template 模式的适配器发现逻辑中加一个分支。
当时无法确定改动验证器的发现逻辑是否触及 v1 稳定表面——若触及，就必须走
`docs/versioning.md` 中的主版本流程。

决策：把「多识别一个适配器表面」的发现逻辑新增，视为向后兼容的 minor 变更，
本次以 `1.1.0` 发布。该规则可推广：多识别一个表面属于 minor，因为任何既有仓库
都不需要改动文件、映射或读取顺序就能继续通过校验。只有当它不再识别某个原本
合法的表面，或使原本通过的仓库开始失败时，才构成 breaking。

后果：未来新增适配器沿用同一路径，不需要主版本。采用映射的契约版本保持为 1，
因为 `aews.json` 的 schema 未变。`1.1.0` 的发布说明与 readiness 记录仍属 owner
控制的发布准备工作。

Evidence: `docs/versioning.md`, `scripts/aews_validate.py`

### 2026-08-08：对内工作文档使用中文，对外契约保持英文

Status: Accepted

Scope: Repo

背景：owner 用中文思考和写作，`TODO.md` 早已是中文，`README.zh-CN.md` 也已加入。
但 AEWS 是一个公开标准，英文是其对外身份；把整个仓库转为中文会显著削弱国际
可读性，而这恰恰与「目前尚无任何外部采用证据」这一已知短板相冲突。

决策：按受众划分语言，而不是按目录划分。对内工作文档使用中文：`PROJECT.md`、
`DECISIONS.md`、`HANDOFF.md`、`TODO.md`、`docs/roadmap.md`、`docs/vision.md`。
对外契约与采用者要读的内容保持英文：`standard/`、`templates/`、`adapters/`、
`examples/`、`CHANGELOG.md`、`CONTRIBUTING.md`、`docs/` 下的采用与验证文档，
以及 `docs/releases/`。`README.md` 保持英文主版本，中文走 `README.zh-CN.md`
译本模式。

后果：owner 每天读写的文档变得更省力，而采用门槛不受影响。代价是验证器的重复
句检测对这些中文文档实际失效——英文适配器与中文文档不会有相同句子，且
`_statements()` 的 60 字符阈值对中文而言远高于对英文，因此这些文档的重复内容
改由人工评审。判断某份文档属于哪一侧的依据是受众，不是它所在的目录。

Evidence: `PROJECT.md`, `HANDOFF.md`, `docs/roadmap.md`, `docs/vision.md`,
`README.zh-CN.md`
