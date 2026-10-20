# 从叙事意图找音乐片段

用于选曲、编排与替换配乐。先确定这一段让观众怎样变化，例如从怀疑到好奇、从观察到行动、从紧张到释然。给声音职责、需要的时长、旁白密度、视觉落点与希望避开的质感，再检索。整曲贯穿、同曲不同段、跨曲组合和静默都可以成立，不强制三首或三幕。

## 音乐图册与 Agent 查询

读取 `catalog/music.json` 的 taxonomy 或执行查询，按需查询已添加的曲目。`assets/music/index.html` 是自包含图册，支持按八类场景、情绪、叙事职责搜索，波形、变化点与候选片段定位。图册不含原始歌曲；导入本机 registry 后才可尝试原文件试听。浏览器/宿主不能播本地文件时保留未验证状态，不绕过其安全限制。

```text
python3 SKILL_ROOT/scripts/music_library.py search --scenario product-demo --emotion curious --role establish --narration --avoid-bright --limit 5
python3 SKILL_ROOT/scripts/music_library.py search --scenario brand-film --role payoff --energy high --limit 5
python3 SKILL_ROOT/scripts/music_library.py get your-track-id --registry /project/music-registry.local.json
python3 SKILL_ROOT/scripts/music_library.py health --registry /project/music-registry.local.json
python3 SKILL_ROOT/scripts/music_library.py validate-sheet /project/music-cue-sheet.json --registry /project/music-registry.local.json
```

查询返回片段，不只返回歌曲；情绪、用途是导演建议，排序分数不是审美质量。查无匹配时放宽一个条件、试听同曲其他段或找获准的新音乐，不强配。曲内 relative_energy 与整曲 arousal 分开；前者是相对信号强弱，后者是待试听的情绪唤醒建议。低频谱占比不等于声音一定舒服，无人声初筛不等于无旁白遮蔽。

公开版的音乐目录为空，保留场景、情绪与叙事职责分类。使用者先添加获准曲目、真实文件哈希、实际时长与候选片段，再执行查询。不附带歌曲或会员曲库数据。

分析、导演推断与实际试听分别记录；没有测量或听审的数据保持未验证。

## 选段与编辑判断

先用少量候选试配故事，不边浏览边盲目增加曲目。库中 source_in/source_out 是真实原文件秒数，片段可能是较疏的陪衬、较强的推进、能量建立或回落候选；并非宣称已找到副歌或“最佳片段”。入点附近的低能量/低变化点仅便于粗剪，最后要检查旋律是否被截断、第一击是否突兀、尾音是否被切掉。留前后handles，在必要时重找完整乐句。

按内容决定是否连续使用同曲。换曲需要有叙事理由，例如从问题转向系统能力，再落到人的收益。保持共同的节奏动机、音色或空间感，也可以用动作声、环境接桥或有意静默隔开。没有测拍、测调时不声称同调同拍，不直接做长时间旋律叠加；简单淡化也要试听重叠区。需要变速、循环或重编曲时单独记录实现与听审，不默认把任何段落拉成任意长度。

科技感可来自节奏秩序、分层空间、低中频的尺度与精确反馈。出现声音尖锐或配乐单调时，同时检查音色、段落对比和叙事发展；不要靠把所有轨道变亮、变响来制造科技感，也不要只靠随机音符或同一循环铺满全片。

## Cue sheet 和两套时钟

使用 `templates/music-cue-sheet.json`，项目内保存一份实际数据。每次放置有唯一id、track_id、cue_id、source_sha256、source_in/out、timeline_start/end、叙事职责、淡入淡出与衔接理由。原曲时间与整片时间明确分开，区间为左闭右开。默认不变速，两段长度应相等；交叉淡化造成的重叠要计入成片时钟。完整曲可不填cue_id，source范围覆盖实际使用段。

不改变原plan合同：最终生成的裁剪/混音文件作为plan.assets，scenes.audio_cues按整片绝对时间引用实际文件；cue sheet作为可编辑源记录原曲溯源与剪辑。`validate-sheet`核来源、时钟、hash与重叠理由，不证明声音已渲染、同调、舒服或音画落点正确。权限、缺失素材与未听分别列出。

## 素材位置、来源与扩展

Skill存索引、标签与方法，不分发付费音乐。本机文件在registry的assets内以track_id关联path/sha256/duration_seconds；优先使用 `--registry`、其次 `CJF_VIDEO_MUSIC_REGISTRY`，否则查当前用户数据目录 `$XDG_DATA_HOME/chaojifeng-video-design/music-registries/<library_id>.json`（未设变量时为 `~/.local/share` 下同一位置）。新宿主没有登记时明确缺失，不猜音源路径。缓存随时可能清理，使用前health检查；不把路径存在当永久保管或授权证明。迁移后以内容hash核对，不凭同名文件静默替换。

添加曲目前核对来源与项目用途许可，并留证。会员身份不自动代表外部剪辑、商用或再分发许可。

扩展任意合法本地音乐时沿用schema与taxonomy，可增加必要标签并写定义；保留来源、许可、hash和分段依据。先做实际音轨分析，再给用途解释，不能按曲名批量宣称逐首听审。运行 `validate-catalog`，再针对本片试听和渲染。空目录是有效初始状态，不把作者的私人曲库当作运行依赖。

方法依据：[AudioLabs 音乐结构分析](https://www.audiolabs-erlangen.de/resources/MIR/FMP/C4/C4S4_NoveltySegmentation.html)解释局部变化与段落候选；本库使用更轻的前后特征差启发式，未实现其完整SSM流程。[FFmpeg滤镜](https://ffmpeg.org/ffmpeg-filters.html#atrim)提供裁剪和接桥实现参考，实际参数先核当前工具支持。涉及剪映素材时参考[剪映素材协议](https://sf1-cdn-tos.douyinstatic.com/obj/ies-hotsoon-draft/vco/f72e9cd9-cc19-4db7-ba74-0794833ce854.html)来源，不替代逐项使用范围核查。
