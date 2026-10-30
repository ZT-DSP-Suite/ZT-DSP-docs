# isostress 协议文档

## 这里有什么

规范正文、术语表、符合性判定指南、开发与验证指南、许可与声明。

## 按什么找

见下方文档地图，按你要做的事分六条路径。

**中文** ｜ [English](en/README.md) ｜ [术语对照表](cn/术语对照表.md)

> isostress 是一个在网络不可信前提下建立可信通信的协议。本仓库是它的文档仓库。

## 目录结构

本仓库的文档以**双语镜像**方式组织：

| 目录 | 说明 |
|---|---|
| `cn/` | 中文文档（规范正文、术语对照） |
| `en/` | English documentation — 规范、术语表、判定指南与开发指南都有对应英文版 |

英文版与中文版一一对应，对应关系如下：

| 中文 | English |
|---|---|
| `cn/README.md` | `en/README.md` |
| `cn/术语对照表.md` | `en/Glossary.md` |
| `cn/spec/isostress-1.0.0-总指导.md` | `en/spec/isostress-1.0.0-Master_Guide.md` |

新增或修改文档时，两侧必须同步；**只改一侧视为缺陷，不视为贡献**。

## 文件

| 文件 | 它是什么 |
|---|---|
| [cn/README.md](cn/README.md) · [en/README.md](en/README.md) | 中英文入口 |
| [规范（中文）](cn/spec/isostress-1.0.0-总指导.md) · [specification](en/spec/isostress-1.0.0-Master_Guide.md) | 协议正文，含第零部分与附录 B、C、F–K；未设 A、D、E |
| [术语对照表](cn/术语对照表.md) · [Glossary](en/Glossary.md) | 术语的唯一出处 |
| [符合性判定指南](cn/CONFORMANCE-GUIDE.md) · [Conformance guide](en/CONFORMANCE-GUIDE.md) | 一次实现是否合规的判定方法 |
| [开发与验证指南](cn/DEV-GUIDE.md) · [Dev guide](en/DEV-GUIDE.md) | 构建与验证命令 |
| [LICENSING.md](LICENSING.md) · [LICENSE](LICENSE) | 许可条款 |
| [TRADEMARK.md](TRADEMARK.md) | 标识 |
| [CONTRIBUTING.md](CONTRIBUTING.md) · [CONTRIBUTORS.md](CONTRIBUTORS.md) | 贡献方式与署名 |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | 行为准则 |
| [SECURITY.md](SECURITY.md) | 漏洞上报 |
| [CHANGELOG.md](CHANGELOG.md) | 变更记录 |
| [PUBLICATION-RECORD.md](PUBLICATION-RECORD.md) | 公开指针与专利不主张声明 |

完整发布记录与标识源文件由维护者保存；本仓保留公开指针与专利声明。

## 相关仓库

| 仓库 | 内容 | 版本标签 |
|---|---|---|
| `isostress-docs` | 本仓库：协议规范、术语基线 | `docs-v*` |
| `isostress-client` | 参考实现：`isostress_py/`（Python，实现标识 `ISOSTRESS_PY-1.0.0`）与 `isostress_rs/`（Rust，实现标识 `ISOSTRESS_RS-1.0.0`） | `client-v*` |

## 许可

本仓库的规范正文以 **CC BY-SA 4.0**（署名—相同方式共享）授权：照规范写实现不受限制，引用须署名；翻译与改写都属改编，译本与改过的规范必须同样开放（仅约束文档本身）。详见 [LICENSING.md](LICENSING.md) 与 [LICENSE](LICENSE)。
