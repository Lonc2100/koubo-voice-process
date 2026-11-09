# 人声自然度与响度

`koubo-voice-process` v0.1.0。面向亲自录制口播、希望AI协助后期的人。由实际口播制作的规则与验收方法整理，公开的是脱敏工作流，不是完整自动剪辑软件。

## 能做什么

请用相机原始音轨整理人声音量，保留自然咬字，原声和候选同句同速同响度试听。

## 开始使用

安装：`npx skills add Lonc2100/koubo-voice-process --skill koubo-voice-process`。或从Releases下载ZIP，解压到客户端支持的Skill目录，确认能发现`koubo-voice-process`。首次先用一段自己的短素材试跑。

> 请用相机原始音轨整理人声音量，保留自然咬字，原声和候选同句同速同响度试听。

宿主须支持读取SKILL.md及相对文件。转写、FFmpeg剪辑、字幕渲染和音频模型等执行能力需由自己的客户端提供；本包不会替你安装模型或获得账号权限。普通网页聊天没有本地文件权限时不能直接处理硬盘素材。需要付费能力时先核费用与外发许可。

## 输入、输出和检查

提供有权使用的原片/锁定逐字稿、当前版本、作者要求与运行条件。交付相应任务产物、来源及决定、可回查的时间映射、实际验收范围与未验项。具体步骤见[SKILL.md](SKILL.md)和[共同标准](references/standards.md)。文件存在、命令成功与作者听懂/听感认可分别判断，不能保证爆款或同款音色。

## 与内部制作工程的关系

公开版继承对应职责的原话/真实性边界、制作判断和验收方法，增加可独立阅读入口；不复制内部作品路径、作者录音、他人素材、完整工程、字体或模型。它不宣称带齐内部所有专项脚本；这些差别写清而不以安装成功代替端到端制作验证。

## 问题排查

未触发：确认客户端支持Skill、根目录直接有SKILL.md并重新加载。素材读不到：先核绝对路径和本地权限；工具缺失：看具体报错及客户端环境。不要把识别文字当听审，不反复处理已经加工过的混音。

## 许可证

MIT，见LICENSE。自己的输入素材与第三方工具许可另行负责。本包没有媒体、密钥、模型权重。

## Prerequisites
- [ ] Client supports SKILL.md and local files.
- [ ] You own or are permitted to process the input media.
- [ ] Required transcription, rendering and audio tools are available separately.

## Natural-language examples
- “请使用这个Skill处理我提供的当前版本，先核来源和输入条件。”
- “按这个Skill检查产物，说明实际验证范围和未通过之处。”

## Verification
```sh
python -m unittest discover -s tests
```
Structure/link tests only; author hearing and viewing still matter.

## Troubleshooting
If not discovered, verify the root SKILL.md location and reload your client. If a required media tool is absent, report it and install through your normal authorized process; do not fabricate completion.

开发维护可使用技能工厂的 validate_skill.py 做结构检查；该检查器不是运行依赖。

## 你可以直接这样说

请使用 koubo-voice-process，按上面示例处理我的素材并说明未验项。
