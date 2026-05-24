# 个人博客仓库

这是一个基于 `MkDocs + Material for MkDocs` 的个人博客项目仓库。

## 当前结构

- `mkdocs.yml`：站点主配置
- `docs/`：博客页面、静态资源、主题覆盖模板
- `scripts/mkdocs_hooks/`：MkDocs 构建阶段使用的自定义 hooks
- `projects/`：不直接参与站点构建的独立代码项目与实验代码
- `博客优化.md`：项目结构分析与优化建议
- `博客重构记录.md`：已实施的重构记录与校验结果

## 维护原则

- 页面和静态资源放在 `docs/`
- 模板覆盖放在 `docs/overrides/`
- 构建逻辑放在 `scripts/mkdocs_hooks/`
- 独立代码项目放在 `projects/`

这样可以尽量避免内容、模板、脚本、项目代码继续混放。
