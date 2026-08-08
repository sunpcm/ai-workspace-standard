# PROJECT

## 用途

AI Engineering Workspace Standard（AEWS）定义了一种极简、与代理无关的方式，
用于为 AI 辅助开发组织工程知识。

本项目关注持久的工作区知识、文档生命周期、范围边界、向工具专属适配器文件的
轻量投影，以及代理之间可选的、有证据支撑的连续性。

## 范围

- Scope: Workspace standard
- 当前版本：v1.1.0 本地候选版；v1.0.0 已发布
- 主要受众：在多个仓库中使用多个 AI 编码代理的工程师
- Primary 兼容目标：Codex 和 Claude Code
- Secondary 兼容目标：GitHub Copilot
- 扩展策略：保持适配器契约与厂商无关、对其他工具开放，但当前不承诺为它们
  投入实现或运行时验证

## 架构

AEWS 有两层：

- 规范标准：`docs/`、`standard/`、`templates/` 和 `examples/`。
- 代理适配器：`adapters/` 以及轻量的根级代理入口文件。

规范标准是事实来源。适配器应当引用规范文档，而不是复制它们的内容。

跨代理连续性是叠加在这些来源之上的一层文档协议。Git 与已验证的工件确立实现
状态；可选的 harness memory 可以承载一次交接，但不构成受治理的事实。

Codex 和 Claude Code 是 owner 的主力工具，并携带受控的运行时加载证据。
GitHub Copilot 是被积极使用的辅助工具，有维护中的适配器，但不作运行时证据
声明。现有的 Cursor 与 Gemini 投影仍是有用的参考实现，但不构成当前的开发或
运行时验证承诺。

## 命令

```bash
# Inspect files
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print

# Check for large markdown files
wc -l README.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md

# Search for adapter references
rg -n "AGENTS.md|CLAUDE.md|GEMINI.md|PROJECT.md|HANDOFF.md|DECISIONS.md"

# Inspect local adapter runtime availability without invoking a model
codex --version
claude --version

# Run the read-only validator
python3 scripts/aews_validate.py . --mode template

# Run validator regression tests
python3 -m unittest discover -s tests -p 'test_*.py' -v

# Check the English contract surface is still complete
python3 -m unittest tests.test_language_boundary -v
```

## 验证

在认为改动完成之前，确认：

- 根 `AGENTS.md` 保持轻量，
- 规范概念位于 `docs/` 或 `standard/` 之下，
- 模板保持最小，
- 适配器没有复制持久的架构内容，
- 启用连续性 profile 时，已声明的适配器都路由到同一个活跃 handoff 和任务
  队列，
- 示例不依赖脚本也能读懂，
- 变更文件通过 `docs/validation-checklist.md`，
- `python3 scripts/aews_validate.py . --mode template` 无 failure 也无 warning，
- 回归测试通过，其中 `tests/test_language_boundary.py` 确认英文契约面完整。

## 已知风险

- 如果过早加入 hooks、MCP、安全和运行时特性，项目会漂移成 ECC 式的 harness。
- 如果投影规则得不到执行，适配器文件会变成重复的事实来源。
- 如果不慎重对待 Global 范围，个人偏好会泄漏进公开模板。
- 过期的 handoff 会误导另一个代理，除非它被 Git 和测试核对过。
- 同一个 worktree 中的并发代理会覆盖或误提交彼此的改动；请使用独立分支或
  worktree。
- 如果把非主要工具的参考投影误当成已验证集成，兼容性表述会被夸大。
- 中文的工作文档不再与英文适配器共享句子，因此验证器的重复句检测对这些文档
  实际上不再生效；重复内容需要人工评审。
- 英文契约文档若只用链接引用中文工作文档，会让英文读者的证据链断掉；引用时
  必须在英文侧自带结论摘要。
