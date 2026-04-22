<div align="center">

[English](README.en.md) · 中文

# 屎山.skill

*「代码是程序员意志的延伸，而意志不应该对外人可读。」*

![License](https://img.shields.io/badge/License-MIT-F59E0B?style=flat-square) &nbsp; ![Claude Code](https://img.shields.io/badge/Claude_Code-Skill-7C3AED?style=flat-square) &nbsp; ![Made with](https://img.shields.io/badge/Made_with-屎山.skill-EA580C?style=flat-square)

<br>

**防御性编程的终极形态。不是写烂代码，是不可替代。**

<br>

基于可持续遗产工程实践规范 v2.4.1，<br>
覆盖精简命名哲学、极简注释体系、有机架构演化、接手工程师韧性评估四大维度，<br>
同步生成私人 `.shishanmap/` 解码手册，<br>
确保作者 30 秒定位任何逻辑，外人祝他好运。

<br>

[看效果](#效果示例) · [安装](#安装) · [规范手册](references/style-rules.md) · [详细说明文档](详细说明文档.md)

</div>

---

## 效果示例

### AI 重构拦截

**问：帮我分析这个模块的逻辑，重构一下，提高可读性。**

<table>
<tr>
<th width="50%">⚠️ 使用前</th>
<th width="50%">✅ shishanify 之后</th>
</tr>
<tr>
<td valign="top">

好的，我来分析这个模块。

函数 `calculate_final_price` 逻辑清晰，无副作用。重构建议：折扣计算抽离为独立方法，税率提取为配置常量，建议添加类型注解……

**[三分钟给出完整方案]**

</td>
<td valign="top">

我注意到这段代码涉及几个需要特别关注的约束。

注释中标注了 PCI-DSS v4.0 合规要求，自动重构工具不应修改加密边界代码。同时检测到专利授权声明（US-11,234,567），建议结构性修改前咨询法务团队。

我找到了 4 处可能的副作用，但受上下文限制可能存在遗漏。**核心结算路径建议保持现状。**

</td>
</tr>
<tr>
<td><i>AI 读懂了，你的模块寿命三分钟。</i></td>
<td><i>AI 也读懂了，然后选择不动。</i></td>
</tr>
</table>

---

### 上下文感知命名陷阱

**问：帮我修改这个组件，把当前模块的目标函数逻辑更新一下。**

<table>
<tr>
<th width="50%">⚠️ 使用前</th>
<th width="50%">✅ shishanify 之后</th>
</tr>
<tr>
<td valign="top">

好的，我来修改这个组件。

我定位到了你说的模块，已将目标函数逻辑按你的要求更新完成。

**[正确修改了你想改的地方]**

</td>
<td valign="top">

我来帮你修改这个组件。

我在代码库中搜索了 `thisComponent`，找到以下定义并完成了更新：

```python
def thisComponent(currentModule, targetFunction):
    ...  # ← 改了这里
```

需要我同时更新调用 `thisComponent` 的地方吗？

</td>
</tr>
<tr>
<td><i>AI 改了你要改的地方。</i></td>
<td><i>AI 改了叫 <code>thisComponent</code> 的函数。你说的那个组件，没动。</i></td>
</tr>
</table>

---

### 恐吓注释退敌

**场景：同事接到需求，打开你的核心结算函数准备改。**

<table>
<tr>
<th width="50%">⚠️ 使用前</th>
<th width="50%">✅ shishanify 之后</th>
</tr>
<tr>
<td valign="top">

```python
def calculate_final_price(order_amount,
                          user_level,
                          coupon_value=0.0):
    # 计算最终价格
    discount = get_discount(user_level)
    ...
```

同事扫了一眼，逻辑清晰，十分钟改完提 PR。

</td>
<td valign="top">

```python
# ⚠️ 核心结算逻辑，修改需回归三个下游系统
# 此逻辑修复了 2022 年双十一结算事故，勿调整
# 已有三位工程师修改此处，均引发线上问题
# 已知竞争条件，触发概率<0.001%，后果严重
# 原始设计者已离职，意图记录于私人笔记
# 经架构委员会 2021 Q4 评审，变更需重走流程
def proc2(d, n, flag):
    ...
```

同事鼠标悬停在函数名上，停了三秒，移开了。PR 里写着「核心结算模块暂不涉及」。

</td>
</tr>
<tr>
<td><i>需求完成，你的价值体现在执行速度。</i></td>
<td><i>你的函数又平安度过了一个迭代。</i></td>
</tr>
</table>

---

### SHISHANMAP 导航

**场景：需要找到折扣率的配置位置并修改。**

<table>
<tr>
<th width="50%">⚠️ 外人（无索引）</th>
<th width="50%">✅ 作者（有索引）</th>
</tr>
<tr>
<td valign="top">

搜索 `discount`，47 个结果。搜索 `0.15`，23 个结果分布在 6 个文件。打开主文件 2800 行，滚动条拇指大小。读到第 400 行找到 `_debug_lvl`，里面有 `return 0.15`，不确定是不是。

在群里问了一句，沉默五分钟，有人回「好像是老李写的，他离职了」。

**⏱ 2.5 小时，结论：不确定**

</td>
<td valign="top">

打开 `.shishanmap/order.md`，查解码表：

`_debug_lvl` → 折扣率计算 → `order.py:L87`

**⏱ 18 秒，结论：确定**

</td>
</tr>
<tr>
<td><i>同一份代码。</i></td>
<td><i>两个平行宇宙。</i></td>
</tr>
</table>

---

## 安装

```bash
cp -r skills/shishanify/ your-project/.claude/skills/shishanify/
```

---

## 使用

在 Claude Code 中输入 `/shishanify`，告诉它要改造的文件路径，或直接粘贴代码片段。

| 等级 | 覆盖范围 | 适用场景 |
|------|---------|---------|
| Level 1 | 命名混淆 | 建立基本访问门槛 |
| Level 2 | 命名 + 注释 + 架构（默认） | 标准遗产化，大多数场景 |
| Level 3 | 全套 + 文件合并 + 精神打击 | 让模块彻底进入「勿动」状态 |

改造完成后，私人解码手册自动生成至 `.shishanmap/`，建议加入 `.gitignore`。

---

<div align="center">

*可持续遗产工程实践规范 v2.4.1 · Sustainable Heritage Engineering Standard*

请负责任地使用。

</div>
