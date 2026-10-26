# 维护与扩展

普通制作在用户项目内完成。新增或修改库本身的规范、能力和默认行为，先遵守宿主授权；单片的临时选择不自动成为长期规则。

## 新增或派生一个风格

先查当前目录能否参数化。稳定变体使用新 ID 和外置集合：

```sh
python3 scripts/stylepacks.py init brand-ink --into /project/video/styles --extends opuscar-ink-wash
python3 scripts/stylepacks.py resolve brand-ink --style-root /project/video/styles
python3 scripts/stylepacks.py validate --style-root /project/video/styles
python3 scripts/catalog.py --kind style list --style-root /project/video/styles
python3 scripts/validate_plan.py /project/video/plan.json --style-root /project/video/styles
```

init 只建立起点，不覆盖现有包。写清本包的材质、色彩、字形、运动、相机、声音、原生动作、避用和回退，核实际品牌、中文、画幅与阅读窗。改版保持本包身份和调用方稳定；改变核心媒介时采用新 ID。

有可复用实现时，登记实际文件、参数、依赖与可运行命令，将小素材来源写清。关键帧、短片、完整导出、观看和听审按实际状态登记。没有可运行实现仍可作为 guidance 收录，不填占位视频或继承来源证据。

## 生成与检查

```sh
python3 scripts/stylepacks.py build
python3 scripts/stylepacks.py build --check
python3 scripts/stylepacks.py validate --sources
python3 scripts/build_gallery.py
python3 -m unittest discover -s scripts -p 'test_*.py'
```

style.json 是风格元数据唯一来源；catalog/styles.json 与 styles/README.md 由 build 生成，图册再由 catalog 构建。不手改生成区。生成内置目录始终排除外置项目与个人集合，防止其内容混入分发包。

## 导入或更新上游

当前锁定 lemomo-ai/lemo-opuscar 的 `413a6bd6d78ebd3bdd5abaec9538a26867f890df`。先研究版本增量、许可证、兼容性与工作流差异，再修改导入器的固定版本与适配规则；不在普通制作时自动拉取 latest。

import_opuscar.py 从已核实的本地 Git checkout 导入，检查 HEAD 与已跟踪文件是否被改动；使用 checkout 中的 styleboard/catalog.json。它不安装、不联网、不执行上游代码。稀疏 checkout 支持只取所需文本源码；传入的 checkout 必须包含要收录的文件。

```sh
python3 scripts/import_opuscar.py --source /path/to/inspected-checkout
```

已有来源包必须在审查变更后显式 `--replace`。导入器保留本库旧包；写入上游完整 STYLE、DEMO、源元数据、可用文本源码与 CREDITS，字体、音源、图片、视频、模型和数据集留在使用项目按授权准备。共享 core 也只是源码，不承诺直接运行上游 build.sh。manifest.json 记录逐文件哈希，validate --sources 核完整性。

上游 AGENTS 保存为 AGENTS.upstream.md，避免作为本工程代理规则加载。第三方源码保持原样，实际适配写在本包 STYLE.md 和项目中，许可证随包保留。新增上游代码后按它的依赖、资源和素材声明检查缺口。

## 其他能力

新增场景、动效、表达与配方沿用 [扩展合同](references/extension.md) 和 [计划合同](references/plan-contract.md) 的现有数据接口；复用稳定 ID、参数单位、能力、冲突、回退及证据字段。它们与风格按语义组合，不为一次参考效果新增近义目录或强制引擎。

修改接口后回归旧计划、外置风格加载、名称冲突、依赖循环、路径边界和证据隔离；实际引擎和导出测试按变更风险选择，资源密集任务串行。
