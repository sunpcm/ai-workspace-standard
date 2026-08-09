# 发布文档模板

准备发布时复制下面两份骨架。每次发布产出两份职责不同的文档：

| 文件 | 受众 | 职责 | 语言 |
| --- | --- | --- | --- |
| `docs/releases/vX.Y.Z.md` | 采用者 | 说明改了什么、保证什么；作为 GitHub Release 正文 | 英文 |
| `docs/releases/vX.Y.Z-readiness.md` | 维护者 | 证明发布提交已就绪，以及哪些没被验证 | 中文 |

两者必须分开。发布说明提出主张，readiness 记录为主张背书。

语言差异不是随意的：发布说明会通过 `gh release create --notes-file` 变成公开
页面正文，readiness 则是仓库内的审计记录。判据是**文档最终出现在哪里**。若需要
中文发布说明，加 `docs/releases/vX.Y.Z.zh-CN.md` 译本，不要替换英文原件。

本模板是本仓库自己的发布脚手架，不属于 AEWS 标准表面，因此修改它不需要版本号
变更，也不对采用方仓库提出任何要求。

## 规则

- 记录实测结果，不要照抄。即使上一版通过了同样的检查，也要针对**本次实际的
  发布提交**重跑每一项。
- 写明版本类别，并引用 `docs/versioning.md` 中支撑它的**具体条款**。「因为是
  新增所以是 minor」是主张，不是论证。
- 绝不把结构性验证当成运行时证据。某个目标没有受控探针，就在两份文档里都写
  明这一点。
- 必须填写「已知限制」。空着的限制段几乎总意味着漏审，而不是真的干净。
- 不修改已发布的发布文档。修正记入下一版和 `DECISIONS.md`。
- 发布动作始终由 owner 执行。准备提交不推送、不打标签、不发布。
- 不要用检查自身搜索的词去命名检查项。用扫描关键词做表格行标签，会让发布记录
  匹配到自己的隐私扫描，进而被迫增加排除项、缩小扫描面。
- 英文文档若引用中文 readiness，必须在英文侧自带结论摘要，不能只给链接。

---

## 骨架一：发布说明（英文）

```markdown
# AEWS vX.Y.Z

One paragraph: what this release adds, and its compatibility class.

## Highlights

- Three to six bullets. Each states a user-visible change, not an internal edit.

## Evidence Boundary

What is proven, what is claimed, and what is neither. Name any target that is
maintained without runtime evidence.

## Upgrade From vA.B.C

What an existing adopter must do. Write "No action is required" when true, and
give the optional copy commands when a new file is available.

The full release audit is recorded in `docs/releases/vX.Y.Z-readiness.md`,
which is written in Chinese.
```

## 骨架二：Readiness 记录（中文）

```markdown
# vX.Y.Z 发布就绪审计

## 结果

- 状态：发布内容已定稿；对外发布由 owner 执行
- 审计日期：
- 审计基线：
- 发布提交：包含本记录的那个提交，用以下命令解析
  `git log -1 --format=%H -- docs/releases/vX.Y.Z-readiness.md`
- 已发布的前一版本：
- 版本类别：major | minor | patch，附 `docs/versioning.md` 中的支撑条款

## 变更内容

| 变更 | 类型 | 表面影响 |
| --- | --- | --- |
|  | 新增 / 修改 / 移除 | 既有仓库必须做什么，或什么都不用做 |

说明上一个主版本 readiness 记录里的稳定表面是否未变，以及分类理由记在哪里。

## 验证结果

| 项目 | 结果 |
| --- | --- |
| Git 范围与提交历史 |  |
| `git diff --check` |  |
| 根目录校验 |  |
| runtime fixture 校验 |  |
| 回归测试 |  |
| runtime fixture 哈希清单 |  |
| 适配器行数 |  |
| 凭证扫描 |  |
| 个人路径扫描 |  |
| 私有上下文扫描 |  |
| 运行时与 harness 边界 |  |
| 推送、打标签与公开发布 | 待 owner 执行 |

## 兼容性证据

| 目标 | 层级 | 证据 | 边界 |
| --- | --- | --- | --- |

只有 Primary 携带运行时加载声明。不要用会把该声明扩展到其他层级的方式总结
这张表。

## 已知限制

- 没有受控运行时证据的目标。
- 探针记录的工具版本早于当前安装版本。
- 刻意排除在范围之外的行为。
- 仍需人工完成的检查。

## 验证命令

粘贴实际执行过的命令，并执行 `docs/release-checklist.md` 第 10 节的隐私扫描。

## 发布顺序

按顺序给出推送、打标签和 GitHub Release 的命令，随后是验证命令。明确写出准备
提交本身不执行其中任何一项。
```

## 它在流程中的位置

`docs/release-checklist.md` 是决定能否发布的可复用关卡。本模板塑造关卡产出的
那份记录。先跑检查表，再用它的**实际结果**写这两份文档。
