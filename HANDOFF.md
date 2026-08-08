# HANDOFF

## 当前目标

发布 v1.1.0，并记录发布后的外部状态。

## 当前状态

- 仓库路径：仓库根目录
- 上一个已完成步骤：把 Primary/Secondary/Extension reference 三层支持策略
  同步到矩阵、标准、证据记录、路线图、检查表和决策；补齐
  `docs/releases/v1.1.0.md` 与 `docs/releases/v1.1.0-readiness.md`；新增
  `README.zh-CN.md` 并修正两份 README 里 v1.0.0 已发布后失效的状态描述；
  按 `docs/releases/TEMPLATE.md` 的规矩为新的发布提交重跑了全部检查与三项
  隐私扫描。
- 最新已完成步骤：把对内工作文档转为中文，并把语言边界落成机制。新增
  `tests/test_language_boundary.py`：新增文档默认按契约面处理，契约面出现
  中文即失败并指出行号，译本必须有英文原件；已用注入中文的方式验证该检查
  确实会失败。同时修复两处缺陷——`CONTRIBUTING.md` 原本把英文读者领进中文
  文件却无提示，`docs/releases/v1.1.0-readiness.md` 原本把版本分类依据只以
  链接指向中文决策，现已在英文侧自带摘要。
- 下一步：`v1.0.0` 已在 `efb1724` 打标签并发布 GitHub Release。推送 `main`，
  在通过审计的发布提交上打 `v1.1.0` 标签并发布，命令见
  `docs/releases/v1.1.0-readiness.md`。中文化提交在该发布提交之后，属于下一个
  版本的内容，不应包含在 `v1.1.0` 标签中。
- 阻塞项：仓库内容无阻塞。执行手动 GitHub Release 命令前，owner 本地的 `gh`
  认证必须有效。

## 证据

```bash
find . -maxdepth 6 -path ./.git -prune -o -path ./ECC -prune -o -type f -print
wc -l README.md README.zh-CN.md AGENTS.md PROJECT.md DECISIONS.md HANDOFF.md docs/*.md standard/*.md
git status --short --branch
git log --oneline --decorate -5
git ls-remote --tags origin
wc -l AGENTS.md adapters/codex/AGENTS.md adapters/claude-code/CLAUDE.md adapters/cursor/.cursor/rules/aews.mdc adapters/gemini/GEMINI.md
wc -l .github/copilot-instructions.md adapters/copilot/.github/copilot-instructions.md
sed -n '1,340p' docs/adapter-matrix.md
sed -n '1,280p' docs/runtime-loading-evidence.md
sed -n '1,320p' docs/releases/v1.1.0-readiness.md
python3 scripts/aews_validate.py . --mode template
python3 scripts/aews_validate.py tests/fixtures/runtime-loading --mode template
python3 -m unittest discover -s tests -p 'test_*.py' -v
shasum -a 256 -c tests/fixtures/runtime-loading/SHA256SUMS
```

## 待决问题

- 是否为 `v0.1.0` 补建 GitHub Release 页面。
- 缺失 Decisions 是否只在仓库显式声明完全遵循 AEWS 之后才算 failure。
- 中文化之后，验证器的重复句检测对这些工作文档实际失效（英文适配器与中文
  文档不会有相同句子，且中文 60 字符阈值远高于英文），是否需要为此调整检查
  或明确改为人工评审。

## 过期条件

任何 owner 控制的发布动作改变当前证据之后，替换这份 handoff。
