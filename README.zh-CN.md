# AI 工程工作区标准

AI 工程工作区标准（AEWS）是一个极简、与代理无关的标准，用于组织工程知识，使其可被 Codex、Claude Code、GitHub Copilot、Cursor、Gemini CLI 以及未来的代理消费，而不会将工作区绑定到某个厂商。

AEWS 将工作区视为持久资产。特定代理的文件只是标准的一种投影，而非事实的唯一来源。

该标准对任何轻量代理适配器保持开放。Codex 和 Claude Code 是主要目标并携带受控的运行时加载证据。GitHub Copilot 是次要目标：被积极使用和维护，但没有运行时证据声明。Cursor、Gemini CLI 以及未来工具为扩展参考，而非活跃的运行时承诺。

## 目标

- 保持工程上下文简洁、精确且与任务相关。
- 在撰写之前决定知识应放在哪里。
- 将规范性工作区知识与特定代理适配器分离。
- 让交接（handoffs）、决策、实验和仓库事实易于维护。
- 避免在多个代理工具之间复制相同的知识。
- 通过共享的、有证据支持的检查点协议，让多个代理能够从相同的项目状态继续工作。

## 非目标

- AEWS 不是 ECC 的克隆。
- AEWS 不是代理运行时、钩子系统、MCP 目录或安全护栏。
- AEWS 不是大量 `AGENTS.md`、`CLAUDE.md` 或编辑器规则文件的集合。
- AEWS 不替代项目文档、测试、CI 或运行手册。

## 核心原则

优先范围（Scope first）：

1. 决定信息属于 Global、Workspace、Repo 还是 Experiment 范围。
2. 决定它是 Knowledge、Decision、Task、Working State 还是 Archive。
3. 然后再决定哪个文档或适配器应该公开它。

## 仓库布局

```
docs/                 可读的人类设计文档
standard/             规范的 AEWS 模型和规则
templates/            最小化的文档模板
examples/             小型参考工作区
adapters/             特定代理的投影
PROJECT.md            该仓库的持久事实
DECISIONS.md          已接受的项目决策
HANDOFF.md            当前的工作状态
AGENTS.md             针对该仓库的轻量 Codex 入口
.github/copilot-instructions.md
                      针对该仓库的轻量 GitHub Copilot 入口
```

## 快速开始

选择一条路径。不要仅为匹配 AEWS 文件名而创建重复的规范性文档。

获取稳定的标准：

```bash
git clone --branch v1.1.0 --depth 1 \
  https://github.com/sunpcm/ai-workspace-standard.git <aews-repo>
```

### 新建或最小化仓库

从目标仓库复制最小的规范性文档，并且只复制实际使用的适配器：

```bash
cp <aews-repo>/templates/repo/PROJECT.md ./PROJECT.md
cp <aews-repo>/templates/decision/DECISIONS.md ./DECISIONS.md
cp <aews-repo>/adapters/codex/AGENTS.md ./AGENTS.md
cp <aews-repo>/adapters/claude-code/CLAUDE.md ./CLAUDE.md
mkdir -p .github && cp <aews-repo>/adapters/copilot/.github/copilot-instructions.md \
  ./.github/copilot-instructions.md
```

保留仓库现有的 `README.md`，或在验证之前创建一个。

然后：

1. 用真实的仓库事实和验证命令替换 `PROJECT.md` 中的每个提示。
2. 在 `DECISIONS.md` 中添加已接受的决策；不要虚构历史条目。
3. 仅在需要共享继续检查点时，复制 `templates/handoff/HANDOFF.md`。
4. 使用仓库现有的问题跟踪器或 `TODO.md` 作为共享任务队列。
5. 删除未使用的适配器。

从 AEWS checkout 进行验证：

```bash
python3 <aews-repo>/scripts/aews_validate.py <target-repo> --mode template
```

### 现有仓库

保留现有的架构、决策和工作上下文文档。复制并编辑路由清单，而不是重命名或复制它们：

```bash
cp <aews-repo>/templates/adoption/aews.example.json ./aews.json
$EDITOR ./aews.json
python3 <aews-repo>/scripts/aews_validate.py .
```

使用外部映射进行首次只读评估：

```bash
cp <aews-repo>/templates/adoption/aews.example.json /tmp/aews-target.json
$EDITOR /tmp/aews-target.json
python3 <aews-repo>/scripts/aews_validate.py <target-repo> \
  --mode adoption \
  --config /tmp/aews-target.json
```

有关迁移决策，请参阅 `docs/adoption-guide.md`；有关每个映射字段，请参阅 `templates/adoption/README.md`。

## 每日多代理工作流

在开始工作时，每个适配器应将其代理路由到相同的：

1. 项目事实和验证命令；
2. 已接受的决策；
3. 活跃的 Handoff（如果存在）；
4. 任务队列；
5. Git 与测试证据。

在一个有意义且经验证的检查点，更新共享任务状态并用已完成步骤、确切证据、下一步、阻塞项和过期条件替换 Handoff。在 `DECISIONS` 中记录持久理由，在 `PROJECT` 中记录稳定事实。不要复制转录或将每个代理的进度历史分别放入任何适配器文件。

对于并发工作，请使用独立的分支或 worktree。AEWS 不提供实时存在或文件锁定。

## 跨代理连续性

AEWS 可以通过将 Codex、Claude Code 以及其他代理路由到共享的 Project、Decisions、Handoff 和任务队列角色，让它们理解相同的项目进展。Git 与测试工件验证实际更改。

这是一种基于检查点的连续性，而非实时存在或转录共享。有关起点、检查点、过时、并发和可选的集成规则，请参阅 `docs/cross-agent-continuity.md`。

## v0.1 可交付项

- 架构：说明 AEWS 为何使用四个范围和一个投影层。
- 文档生命周期：说明信息如何从工作状态转为持久知识。
- 最小模板：repo、handoff、decision 和 experiment 文档。
- 适配器矩阵：说明规范性文档如何映射到 Codex、Claude Code、GitHub Copilot、Cursor 和 Gemini CLI。
- 验证检查表：防止上下文复制和适配器膨胀的人工检查。
- 采用指南：如何以最小改动迁移现有仓库。
- 版本策略：如何评估标准、模板、示例和适配器的更改。
- 路线图：v0.1、v0.2 和 v1.0 应包含的内容。

## v0.2 验证

第一个无依赖、只读的验证器位于 `scripts/aews_validate.py`。有关模板/采用用法、测试过的 `templates/adoption/aews.example.json` 映射、已实现的检查和人工审查限制，请参阅 `docs/validator.md`。

v0.2 还定义了有证据支持的适配器兼容性和可选的跨代理连续性，前提是不复制任务历史或将运行时内存视为项目事实。运行时证据聚焦于 Codex 和 Claude Code，而通用适配器契约保持开放。

## v1.0 稳定表面

AEWS v1.0.0 稳定了范围模型、规范性角色、轻量适配器契约、采用映射版本 1、只读验证器以及可选的检查点连续性协议。`docs/adoption-guide.md` 和 `templates/adoption/aews.example.json` 是最短的采纳路径。

对这一表面的重大更改遵循 `docs/versioning.md`。运行时证据按测试过的工具版本记录，但不会将 AEWS 变成代理运行时。

## 状态

AEWS v1.0.0 已发布。v1.1.0 新增 Secondary 支持层级和 GitHub Copilot 投影；发布说明见 `docs/releases/v1.1.0.md`，审计与限制见 `docs/releases/v1.1.0-readiness.md`。

对相同的公共合成检查点，Codex 和 Claude Code 的受控、版本范围的运行时加载探测均已通过。GitHub Copilot 在没有此类探针的情况下维护。这些结果并不意味着通用版本兼容性或运行时一致性。请把运行时功能保持在核心标准之外。

## 许可证

MIT
