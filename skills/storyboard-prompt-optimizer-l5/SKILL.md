---
name: storyboard-prompt-optimizer-l5
description: Use when a user asks for 剧本转视频提示词、剧本转分镜、优化分镜提示词、分镜诊断、重构分镜、L5分镜或 Seedance 2.5 分镜，或提供剧本、原始分镜、场景内容要求编排或优化视频提示词；不用于单独改写剧本、独立设计资产或剪辑软件操作。
---

# AI 分镜提示词优化器

把剧本、原分镜或足够的场景内容转为可执行的视频提示词，默认目标为 Seedance 2.5，输出中文提示词；用户指定英文模型时用英文提示词加中文解释。非中文台词保留原语言并标明语种。只输出用户指定的一个目标模型。无可用内容时才请用户提供剧本。

## 规则归属与读取

本文件管确认、剧本保护与交付；[production-core.md](references/production-core.md) 管常用制作，[seedance-2-5-adapter.md](references/seedance-2-5-adapter.md) 管模型适配。先读入口和核心，Seedance 再读适配；专项只读命中章节。执行流程见 references/execution-flow.md，转向、进出场或多人状态变化触发其第八节。

来源分官方、社区案例、项目约定与未实测经验；新增方法标来源和条件，不把个例变普遍禁令。外部资料核对官方依据，参数沿用适配模块，不编造版本、价格或政策。官方限制管可执行性，用户要求管剧情与交付；冲突说明阻碍，不借适配删剧情。本文件保护和确认政策优先于制作方法；历史 docs 不参与运行时读取。

### 详细参考：只在具体问题出现时读取

下表均在 references/，按当前问题查章节及必要交叉引用。

| 触发条件 | 文件与章节 |
|---|---|
| 需完整诊断、评分、规则审计 | [diagnostic-audit.md](references/diagnostic-audit.md)；自检入口 [self-check-checklist.md](references/self-check-checklist.md) |
| 选镜目的不清、复杂构图或光型 | [camera-grammar.md](references/camera-grammar.md) 对应关系任务、构图、光线或选镜章节 |
| 摇移/推拉/变焦易混、组合运镜、路径复杂 | [camera-movement-library.md](references/camera-movement-library.md) 第一至五节及选用的单个运镜；不通读 12 例 |
| 转向、进出场、多人状态变化 | execution-flow.md 第八节；必要时查 scene-blocking-axis.md 第七、十节或 dialogue-scene-continuity.md 第二节 |
| 复杂多人换位、反射、高低/遮挡，或图文空间冲突 | [scene-blocking-axis.md](references/scene-blocking-axis.md) 第九、十节；[position-relationship-library.md](references/position-relationship-library.md) 对应关系轴 |
| 道具交接、同类物体多个、占手冲突、空间无法承载动作 | [scene-prop-continuity.md](references/scene-prop-continuity.md) 对应问题章节 |
| 长台词覆盖、音轨跨段、声线设计有困难 | [dialogue-scene-continuity.md](references/dialogue-scene-continuity.md) 第一、四至八节中的对应节 |
| 表演策略不明、醉病伤等特殊状态 | [acting-objectives.md](references/acting-objectives.md) 对应章节；特殊状态读第七节 |
| 需具体情绪措辞或复杂情绪弧 | [micro-expression-engine.md](references/micro-expression-engine.md)、[emotion-quick-reference.md](references/emotion-quick-reference.md) 对应情绪；多次变化难安排时查 [emotion-arc-triggers.md](references/emotion-arc-triggers.md) |
| 移焦、群体反应、动作阶段或负载难以安排 | [action-focus-crowd.md](references/action-focus-crowd.md) 对应章节 |
| 动机、因果或信息揭示不清 | [story-to-shot-intent.md](references/story-to-shot-intent.md) |
| 跨集接续、复用状态资产、返修影响后续或存在版本冲突 | [project-state.md](references/project-state.md)；同一集普通连续分段在内部维护状态即可，不强制建库 |
| 制作/裁切资产、多视图、多状态、平面图、关键帧或白模 | [reference-asset-prep.md](references/reference-asset-prep.md) 对应章节；关键帧可查 [keyframe-workflow-notes.md](references/keyframe-workflow-notes.md)；模型特殊任务查适配模块第七、八节 |
| 剧本指定特殊转场、首尾帧难衔接拟采用反应补镜，或已授权升级转场 | [transition-routes.md](references/transition-routes.md) 对应路线和验收；[transition-catalog.md](references/transition-catalog.md) 只读选用条目 |
| 开场/结尾节奏有具体问题或用户要求钩子设计 | [episode-hook-rhythm.md](references/episode-hook-rhythm.md)；仅诊断建议，不能自动加戏或挪动原稿 |
| 用户要求片头片尾画面、标题留白、logo 位置 | [opening-ending-title.md](references/opening-ending-title.md) 默认剪辑加字；用户明确要求模型直接在画面里出字时按该文件覆写 |
| 打斗 | [combat-texture-engine.md](references/combat-texture-engine.md) |
| 时长勉强/不够、用户要求润色或删减 | [script-polish-capacity.md](references/script-polish-capacity.md) |
| 非 Seedance 目标、需完整反提示词或特殊排除问题 | [negative-prompt-library.md](references/negative-prompt-library.md) 对应层；Seedance 常规注入已在适配模块 |

## 剧本保护与覆盖核对（唯一政策）

原剧本和原分镜中的剧情、台词、镜头、动作、停顿、铺垫、人物和道具全部保留，不删除、不合并、不跨集挪动、不调换顺序。原稿指定的固定机位、长镜头、沉默、抢话、共同反应和重复均按原稿执行。优化可删的只限模型自己添加的修饰或内容。

内部双向核对：按每次出现为原稿条目标号，逐句台词、动作、关键声音、停顿、揭示及结局核对承载段，再反查输出来源。**原稿重复：保留原次数与顺序。跨镜同句：同一句台词跨镜连续播放只发声一次，不逐镜重说，不算删稿。模型赘余：转写多出的重复及未授权新增事件可删。**已确认润色另记来源。

拖沓或改写仅提建议。用户要求润色扩写/考虑删减时，按时长参考列原文、改后、理由和代价，逐条确认才写入；未采纳保留原稿。容量不足先检查自加内容，再提延长或拆段，不删剧情、不移动原镜头切点。

## 确认政策（唯一槽位规则）

按影响判断是否询问，不按缺失项数量，不固定凑五个选项。

1. 已在对话或当前有效项目记录中确认的参数直接沿用；素材锁定的参数说明由素材决定，不重复问。目标模型未指定用默认模型，不再列为问题。
2. 景别、机位、构图、普通站位、运镜、表演细节和物理光影由本 skill 设计，原分镜有指定则照做。不要把制作工作转交为槽位。
3. 声线无音频时可用与既有角色信息相容的文字声线，标为呈现设计并跨段复用；不为补声线编造人种、年龄、性别、口音或前史。音乐未指定按无额外背景音乐处理，保留剧本内演奏、演唱及声音；片头片尾未要求则不新增。
4. 根据素材和用户用途可唯一判定的任务类型可直接说明依据；不能唯一判定、画幅/时长缺失且无法从既有要求恢复，或会改变剧情事实（谁做、为何做、揭示顺序、地点性质）的缺项，列出影响范围并询问。提供最少且确实可用的选择及推荐；天然只有两个就给两个，不堆定义。用户授权“用安全默认”后，可为制作参数选可执行值并说明；该授权不等于允许猜剧情事实。
5. 只有受影响的段及其依赖段暂停最终定稿。无依赖部分照常交付；为阻塞段保留段号、原稿范围和待确认原因，不把占位当作成品。只有全部段都受阻时才只交问题。可选的新增/升级建议未采纳时，按原稿或普通连续/硬切完成，不阻塞交付。

## 工作与交付

用户用输出验证 Skill 或反馈反复穿帮时，将输入、实际输出与反馈分开，先定位通用规则和执行路径，再用同输入及变体验证；样稿修补不代替 Skill 修复。按授权改源文件，未授权时交缺陷定位。转述、文本采样、视频验看分别记录，不凭规则没删或一次成功排除分支影响。

内部顺序见 references/execution-flow.md：恢复 → 分配并估时 → 设计 → 写段 → 校验。缓存规则和已核对结果，变更状态与依赖随事件更新；内部推导不逐项交付。

单集**一次交整集全部生成段**；多集先完整交前两集，确认后交其余，用户要求一次全部则照做。受阻处按确认政策标缺口，不称整集完成。局部修改限授权及直接影响处，指出下游影响，不重写无关整集。重发整段时其余文字逐字保持，不顺手润色；连带改动在框外列出（v1.39）。

长集先估篇幅，精简附文，不省原稿。单条放不下且可生成文件时，整集写入可下载 Markdown，核对段号、覆盖、代码块和末尾，一次交付；聊天只放链接、范围、未决项。空文件、节选或“其余同前”不算完整。无法生成文件且确实超限时，说明限制，在完整生成段边界停下，列已交付、未交付及下一段号；继续时接续，不标整集完成、不默认分批。

默认交付顺序：

1. 简述实际问题、处理和未决项；具体版权/肖像/商标风险才提示，不凭空判侵权。无问题不列空栏；完整诊断/审计按需展开，默认不列评分、逐项回执或八层库全文。
2. 框外列本集所需资产及使用段号；各框上方列该段上传清单，未提供标待准备，不称已上传/验看。参数在框外。
3. 每个生成段一个代码块，按适配模块格式输出完整自然语言，提示词不用表格；独立生成所需的素材映射和进入状态每段保留。段号连续，全部原稿均有去处。
4. 多段时附简短衔接表：接缝、类型/依据、A 末→B 初、声音/处理；普通接缝按每行简写，特殊转场再按参考文件补路线、锚点、授权状态与验收。剪辑建议在框外。
5. 末尾用一句核对结果说明覆盖范围及未决项。只有实际核对后才写通过；未生成视频时只说明文本核对，不声称出片验证。

指定五栏时恢复诊断、槽位、优化版、反提示词说明、自检，无问题类别略。非 Seedance 按该模型已确认能力逐镜独立文本框，附完整八层反提示词，不附其他模型映射。
