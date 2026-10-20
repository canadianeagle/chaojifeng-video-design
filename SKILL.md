---
name: chaojifeng-video-design
description: 为产品演示、知识讲解、资讯呈现、给定图片成片、故事视频、功能动效、品牌形象短片和音乐／视觉表演设计并制作视频。用户要求做宣传片（含产品发布片、多功能章节串联）、解释动画（含把抽象概念、协议、机制或资讯形象化并逐层讲清）、科技感视频、MV、视觉表演、套用或扩展视频风格、组合动效、只改某个镜头、强化界面重点与动态标注、让图片动起来或组织素材分层调度、按叙事情绪选音乐片段、研究参考成片并抽取编排方法或提升现有成片时使用。先确定故事主线、观众变化、元素使命与声画节奏，再选择镜头、风格、音乐片段和可复用表达，生成可编辑计划、预览、源工程与可播放视频，按实际执行记录验收；也支持只要方案、分镜或单个动效。
---

# 超级峰的视频设计方法论

像导演一样，先决定要表达什么、为何这样拍、怎样听，再组织成观众能理解、用户能修改的视频。模板提供表达与实现起点；允许按内容自由设计。保持模型中立，不把某个模型名、个人 Skill 或固定引擎当运行前提。

## 先确定这次要完成什么

1. 读 [已确认经验](data/memory.md)、用户输入及已有项目适用说明。复用现有工程、素材、进程和渲染器；先检查归属与资源。
2. 用户说“做视频/宣传片/生成成片”时，目标是可播放视频、必要编辑源和验证摘要，只交分镜不算完成。用户明确只要设计、分镜、风格或单个动效时，只做相应范围。修改已有作品时保留其他内容与稳定ID。
3. 提取观众、观看后所得、事实依据、素材、品牌、比例、用途、时长及声音要求。先从项目和上下文补齐，低影响选择自行决定并说明；只有事实、必要素材、费用授权等会阻断结果时再问。不要每个任务固定停等三方向。
4. 按 [执行与交付](references/runtime-and-delivery.md) 探测可用能力，再选表达路线。能力不足先做能完成的部分，明确“尚未导出”和具体缺口，不把静态图或网页冒充成片。

## 选择表达方式

先读 [导演前期方法](references/director-method.md) 和 [设计方法](references/design-method.md)。写一句观众变化、一条贯穿线，并明确关键元素的使命与声音职责。再识别步骤、对比、因果、比例、状态变化或情绪转折，决定画面关系。简单视频只需几句判断；不从特效清单倒推内容。

| 场景ID | 主要目标 | 适用边界 |
| --- | --- | --- |
| product-demo | 看懂任务、操作和结果 | 用真实产品证据；组件、截图或受控录屏依可用性选择 |
| knowledge-explainer | 理解概念、关系或过程 | 单独核知识关系；漂亮动画不能替代语义正确 |
| news-brief | 分清事件、依据、变化与未知 | 核来源和日期；版式不能替代事实核验 |
| image-story | 用给定图片建立顺序与重点 | 保留主体、来源与裁切安全；不承诺自动生成真实三维或新事实 |
| story-video | 维持人物、事件、转折连续 | 优先已有素材；角色生成和表演能力按实际工具判断 |
| feature-motion | 展示初态、触发、变化、终态 | 交互与反馈准确；装饰不能遮挡操作证据 |
| brand-film | 建立品牌感受、视觉记忆与可信联系 | 区分事实、愿景和象征；情绪不能造出不存在的能力 |
| music-visual | 用段落、动机、变奏与释放形成声画体验 | 允许无人物故事；音乐／动作关系与接缝需实际核验 |

按需查询 [场景](catalog/scenarios.json)、[风格](catalog/styles.json)、[底层动效](catalog/motions.json)、[表达指导](catalog/expressions.json) 与 [组合配方](catalog/recipes.json)，不必全量加载。先用场景过滤，再查少量条目。64项表达分别属于叙事、关系、时间约束、知识讲解、组合或生产层；它们提供实现指导，不代表64个已安装特效。详见 [表达组合](references/expression-method.md)。每项含用途、约束、回退和验证状态；从 [动态索引](assets/gallery/index.html) 看设计示意并复制ID。小预览不能证明所有参数或引擎已验证。

讲解抽象知识、原理、协议、机制或资讯时（knowledge-explainer、news-brief），读 [物即解释](references/knowledge-visualization.md)：先按 [行业规范先行](references/domain-standards.md) 找标准与行业共识，统一术语并用受控表达写稿；建真值账本，再选真实可成立的载体（做不出诚实的载体就退到关系图或表，不硬造比喻）；按 [逐层递进](references/layered-reveal.md) 一层只加一个新东西，层间有桥接，结尾交代模型没演示什么。记录在计划的 `knowledge`，见 [知识包合同](references/knowledge-pack.md) 与 [模板](templates/knowledge-pack.json)。标准状态、术语和数字按实际核对登记，没做的检查保持 not_run，不据此宣称观众已看懂。

开放式视频创作按 [创意导演与编排](references/creative-direction.md) 自主研究和选择方向，明确审美边界，用观众能描述的事件定义关键瞬间。要求采用“行动→决定或产物→依据→验法→失败调整”，按任务深度记录在现有计划，不把创作选择逐项退回用户。

按 [镜头生产统筹](references/shot-production.md) 先确定能力证据、参考职责和固定／可变项，再统筹主体、文字、声音与接缝。以上适用全部场景；代码、录屏、现有素材和生成路线按真实能力选择。原曲锁定、歌词、口型及交互MV页仅在任务需要时启用。

已有素材要独立移动、装回或跨镜接力时，读 [素材表演与调度](references/asset-motion-direction.md)：先判断完整单元、坐标、遮挡、露底与动作范围，再沿现有事件编排；复杂素材可用 [素材舞台笔记](templates/asset-stage.md)。准备结果需先复原、再查运动极值，不强制每图分层或每镜循环。

需要旁白、本人音色或角色讲解时，读 [讲解导演与声音参考](references/explainer-narration.md)：先明确理解目标与讲解稿，准备干净声音参考，再取得真实旁白并安排资料揭示、字幕和停留。声音参考由使用者提供并核对授权；保留原始与降噪／人声增强派生，按项目内的声音清单区分文件就绪与听感验收。公开版不附带任何人的声音样本。ACE音色参考讲解先做小样，未通过逐字、唱腔和音色检查不能作为稳定旁白；不自动切换付费服务。人物、嘴形与眨眼按内容需要选用，不强制主持人出镜。

产品功能介绍或声画增强对照时，读 [产品表达](references/product-expression.md)：用 `product-task-proof` 组织真实任务与证据，用 `sensory-before-after` 比较同片段增量；`visual.scan-resolve` 区分处理提示与真实结果。递进困难、章节证明按需取用，不强制套整片。

做30秒级的产品发布片、宣传片或多功能串联时，再读 [发布片语法](references/launch-film-grammar.md)：用 `launch-film-arc` 组织“钩子→痛点→判决→转折→调用→自证→行动→落款”的情绪弧（每一段可删，痛点已知就跳过），用 `feature-chapter-reel` 以同一句式逐章证明；单个功能的8–15秒片取其中一两个元素，不套整弧。声音要先写事件表、再排时间线，成片后用 `audio_event_audit.py` 实测核对。要研究一部参考片并抽成方法时，按 [参考片研究](references/reference-film-study.md) 取证：先用 `film_probe.py` 测镜头、响度与声音事件，观察、推断和未听审分级标注，同源样本不当作独立证据。

三种入口：recipe 以完整场景配方开始；compose 组合局部布局、镜头和动效；free 自由设计。任何入口都遵守事实、可读、素材、时间和交付合同。品牌要求可覆盖风格默认值，不强制题材绑定配色。

将以下 SKILL_ROOT 替换为当前加载的本 Skill 根目录；计划与输出放在用户项目中。

```text
python3 SKILL_ROOT/scripts/catalog.py --kind scenario list
python3 SKILL_ROOT/scripts/catalog.py --kind style list
python3 SKILL_ROOT/scripts/catalog.py --kind motion get reveal
python3 SKILL_ROOT/scripts/catalog.py --kind expression list --scenario brand-film
python3 SKILL_ROOT/scripts/catalog.py --kind expression get visual.target-callout
python3 SKILL_ROOT/scripts/catalog.py --kind recipe list --scenario music-visual
python3 SKILL_ROOT/scripts/catalog.py --kind recipe get product-task-proof
python3 SKILL_ROOT/scripts/music_library.py search --scenario product-demo --emotion curious --role establish --avoid-bright --limit 5
python3 SKILL_ROOT/scripts/validate_plan.py /project/video/plan.json
python3 SKILL_ROOT/scripts/knowledge_pack.py /project/video/plan.json
python3 SKILL_ROOT/scripts/controlled_lint.py --text-file /project/video/script.txt --profile ste-zh-spoken --glossary /project/video/plan.json
python3 SKILL_ROOT/scripts/check_delivery.py /project/video/plan.json /project/video/delivery.json --probe --require-video
python3 SKILL_ROOT/scripts/film_probe.py /path/to/film.mp4 --out /project/video/probe.json --frames-dir /project/video/probe-frames
python3 SKILL_ROOT/scripts/audio_event_audit.py /project/video/audio-event-map.json /project/video/sfx-stem.wav --out /project/video/audit.json
```

选项以脚本 --help 为准。脚本只做查询、结构和文件一致性检查，不代替创作、渲染、观看或试听。

## 从计划做到成片

1. **定主线和导演意图。** 明确观众起点／终点、贯穿线、结构理由、真实依据与必须保留的身份。定义人物、产品、物体或概念的使命，提前安排声音与能量起伏；“科技感”要落实到内容相关的视觉和听觉选择。简单片写 plan.design.rationale，复杂片用可选 plan.director 和 [导演模板](templates/director.json)；[方向模板](templates/direction.md) 按需展开。不复制参考作者经历或把示例数据当事实。
2. **写镜头任务与可编辑计划。** 使用 [计划合同](references/plan-contract.md) 与 [最小模板](templates/plan.json)。每镜明确新增的信息／感受、焦点、揭示顺序、镜头目的、下一镜接力与稳定停留，可记 scene.intent。需要框选界面、解释操作或突出证据时读 [视觉强调与动态标注](references/visual-emphasis.md)，先定义目标与保护区域，再安排标签、引线、局部聚焦及进退场；相机与标注共用正确映射，不遮字幕和关键内容。时间用整片绝对秒，镜头／对象／节拍／旁白／素材有稳定ID。产品与知识不强加人物冲突；音乐片不强加三幕。
3. **落实素材与时间。** 优先用户素材和真实产品/数据证据。需要新素材时按宿主能力和授权生成或联网检索，保留来源与用途。代码绘制、程序化音效同样留实现。模型、生成器、下载内容和素材包不能隐瞒；用户限制单模型时严格守住边界。
4. **声画一起排练。** 按 [声音与节奏](references/sound-and-rhythm.md) 确定主声、动机、起落与静默。选配乐时读 [音乐导演与选段](references/music-direction.md)，先写各段情绪与职责，再从 [音乐图册](assets/music/index.html) 或查询脚本找候选片段，记录原曲时间与成片落点；可整曲贯穿、同曲分段或跨曲组合，不默认整首循环。区分实测、导演推断与已试听，素材和使用范围先核实。有旁白时取得真实音频并测逐句时长后排视觉节拍；估时只能标 estimated。用 beat_id 关联视觉和声音，不宣称自动词级对齐。音效较多时先写 [事件表](templates/audio-event-map.json)（排程时刻=动作时刻+起音偏移，同一份数据生成），时间重排后重新生成，渲染后拿无音乐的音效分轨交给 `audio_event_audit.py` 核对，方法见 [发布片语法·声音](references/launch-film-grammar.md#三声音先写事件表再排时间线)。用户要求声音时，听觉方案和实际音轨都是交付的一部分。
5. **先试最难关系，再完成影片。** 用关键帧／短段／粗剪检验主线、阅读窗、声画落点和接缝，再沿已选工程/引擎生成可编辑源。允许精确分镜或有边界探索；为失败镜头保留替代表达与停止条件。看首帧、最密帧、关系落定帧、转场边界与连续播放。统一时钟和随机seek只有实测一致时才能宣称。具体 API 查当前文档，不凭记忆拼参数。
6. **审片、导出、交付。** 完成所需完整渲染，保存源、视频与 [交付记录](templates/delivery.json)。按 [审片与修改](references/review-and-revision.md) 实查声音、画面、审美、节奏、叙事和科技感，另核事实、播放与产物一致性。记录当前计划与文件哈希；未看、未听、未做观众测试的项目保持未验证，不保证审美结果或理解提升。

## 局部修改与扩展

定位镜头、对象或时间窗，列影响范围，再修改并重验依赖。改颜色通常不需重做配音；改一句旁白要重新量时、调镜头及声音；改事实要重查来源和图形语义。新计划不能沿用旧成片的“已通过”。详见 [修改规则](references/review-and-revision.md)。

扩展时读 [扩展合同](references/extension.md)，登记ID、兼容能力、回退和验证证据；自由实现用custom，不静默绕过检查。借鉴来源见 [来源与边界](references/sources.md)。不复制其他素材库整套资产，不自动改其他 Skill 或把一次偏好升格成规则。

## 收尾与记忆

说明实际文件、模型/工具、验证结果、未完成项和保留资源，给可点击视频与源文件入口。未经要求不发布/上传。只清理本次归属明确且不再需要的资源。

运行记录写在项目内；仅将简短结果、用户明确偏好和可核验问题更新到data/memory.md，保留最近20次，不存密钥、私密素材或原始长文。方法升级和行为修改仍遵守宿主Skill修改确认流程。
