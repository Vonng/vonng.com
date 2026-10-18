# Repository Instructions

## OINK build baseline

As of 2026-10-18, this site uses OINK v1.3.2 and Hugo Extended 0.168.0.
Keep CI and local builds on this baseline. Do not enable `--panicOnWarning`
or `HUGO_PANICONWARNING`; keep warnings visible and review them. The upstream
LibSass deprecation warning is accepted. No external Sass compiler is required.

## English Blog Translation Policy

### Scope and file layout

- A blog leaf bundle is a directory under `content/{ai,cloud,db,misc,pg,pigsty,trip}/` containing `index.md`.
- Its English version, when required, must be the sibling file `index.en.md` in the same bundle.
- Section pages, taxonomy pages, author pages, and other non-blog content are outside this translation policy.

### Articles that must not be translated

Leave the following articles intentionally without `index.en.md`:

- `content/misc/fengzhenbiao/` — 冯振彪自传。
- `content/pg/pg-apt-loong64/` — 龙芯相关文章。
- Any Chinese article that is itself a translation or adaptation of somebody else's English article, talk, or publication. Do not translate such content back into English.

Determine whether an article is translation-derived from explicit attribution in the body and front matter, such as an original-source URL, a translation tag, or an external author. Older publication dates and multiple authors are useful clues, but are not sufficient evidence on their own. If the provenance remains genuinely ambiguous after reading the article, report it for confirmation instead of translating it automatically.

### Required English style

For every other original Chinese article that needs an English version:

- Write idiomatic, professional, concise English for a Western technical audience, in the style of a strong Hacker News submission or technical essay.
- Preserve the author's argument, technical meaning, evidence, and distinctive voice. Be concise without turning the article into a summary.
- Prefer direct sentences, concrete verbs, short coherent paragraphs, and restrained wording. Avoid Chinglish, inflated marketing language, bureaucratic phrasing, and ornamental prose.
- Translate ideas rather than surface wording. Recast Chinese idioms, memes, jokes, wordplay, historical allusions, and culture-specific references into an equivalent that works naturally in an English-speaking context. Add a compact explanation when needed; never force a literal translation that sounds awkward or loses the point.
- Use established English technical terminology and Western naming, capitalization, punctuation, date, and number conventions.
- Preserve valid front matter semantics, Markdown structure, code, commands, URLs, images, captions, tables, and other bundle assets. Do not introduce new factual claims or silently remove substantive content.
- Mirror the Chinese front matter key-for-key and in the same order. `date`, `authors`, `images`, and any extra keys stay byte-identical; only `title` and `summary` are rewritten, and the title should read as an English headline rather than a word-for-word rendering.
- Translate each tag to its paired English label in `bin/retag.py`'s `VOCAB` dict, keeping the same count and order. Proper nouns stay as they are. Do not invent a tag that is not already carried by the Chinese article.
- Point an internal link at `/en/<path>/` when the target bundle has an `index.en.md`, and leave the bare path otherwise so it falls through to the Chinese page.

### Per-article workflow and quality bar

- Use one brand-new SubAgent with a clean context for each article. That SubAgent must work on that article only; never batch multiple articles into one translation context.
- Use the highest available reasoning effort. Give the SubAgent the Chinese source, relevant local assets or references, this policy, and the target `index.en.md` path.
- The assigned SubAgent must complete three review passes and three proofreading passes before finalizing:
  1. Check fidelity, completeness, structure, and preservation of nuance.
  2. Check technical accuracy, terminology, names, figures, code, links, and captions.
  3. Check idiomatic English, cultural adaptation, Hacker News tone, concision, and narrative flow.
  4. Proofread grammar, spelling, punctuation, typography, and sentence-level clarity.
  5. Proofread terminology consistency, front matter, Markdown, links, media, and formatting.
  6. Read the entire English article once more as a standalone essay and polish any remaining stiffness, repetition, or ambiguity.
- After all articles are finished, run `make check` (the strict build, which must reach `Total in …` with no WARN), then `python3 bin/check_internal_links.py`, then rescan the leaf bundles for missing `index.en.md` files. Report intentional exclusions separately from actionable omissions.
- These checks verify the work; they do not publish it. Publishing is a separate, explicitly requested step — see *Deployment* in `CLAUDE.md`.

## Git 内容与大文件规则

用户于 2026-10-10 明确的通用仓库规则：

- 仓库默认保存源代码、配置和必要的轻量文档、元数据。构建产物、可执行文件、软件包、容器/虚拟机镜像、下载压缩包、数据库导出和大体积原始数据默认不进入 Git；文本格式的数据大文件同样需要检查。
- 在工作树内下载或生成上述文件之前，先选择仓库外的制品/数据位置，或补上合理的 `.gitignore` 规则并验证实际路径已被忽略，防止暂存和代理恢复/差异快照将它们写入 Git 对象库。
- 暂存、提交前检查新增文件的大小、类型和 staged 文件列表，只加入本次需要的源文件；不得用强制添加绕过忽略规则。优先保留来源清单、校验值及可复现的下载/构建方法。
- 对二进制素材、数据集或生成文件是否应纳入版本控制拿不准时，先问用户，再暂存或提交；确需例外时也先取得用户明确指示。
- 本规则不授权删除已有文件、stash、恢复快照或改写 Git 历史。忽略规则不会清除已存在的 Git 对象，历史清理需要单独明确范围。
