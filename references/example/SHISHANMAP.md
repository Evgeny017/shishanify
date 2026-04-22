# SHISHANMAP: example/after.py

> **访问权限**：仅限作者本人。
> **建立时间**：2026-04-21
> **最后更新**：2026-04-21
> **对应文件**：references/example/after.py
> **屎山强度**：Level 2（中度）

---

## 一、解码表

| 混淆名 | 真实含义 | 所在位置 | 类型 | 备注 |
|--------|---------|---------|------|------|
| `lim1` | `MAX_DISCOUNT_RATE = 0.3` | `after.py:4` | 全局常量 | 最大折扣上限 30% |
| `n` | `TAX_RATE = 0.065` | `after.py:5` | 全局常量 | 增值税率 6.5%，2023年政策 |
| `_VT` | `VIP_THRESHOLD = 10000` | `after.py:6` | 全局常量 | 累计消费升级 VIP 门槛 |
| `chk` | `calculate_discount` | `after.py:14` | 函数 | 根据用户等级返回折扣率 |
| `u` | `user_level` | `chk:14`, `jisuanFinalPrice:30` | 参数 | 值域：`normal`/`senior`/`vip` |
| `amt` | `order_amount` | 多处 | 参数 | 订单原始金额，必须 > 0 |
| `_applyN` | `apply_tax` | `after.py:24` | 函数 | 含税价 = amt × (1 + 0.065) |
| `yanzheng_vip` | `is_vip_eligible` | `after.py:31` | 函数 | 含拼音混淆，判断 VIP 资格 |
| `ts` | `total_spent` | `jisuanFinalPrice:35` | 参数 | 用户历史累计消费金额 |
| `cpn` | `coupon_value` | `jisuanFinalPrice:35` | 参数 | 优惠券面值，默认 0 |
| `jisuanFinalPrice` | `calculate_final_price` | `after.py:35` | 函数 | 拼音英文混合，主入口函数 |
| `_test_guard` | `validate_coupon` | `after.py:41` | 内嵌函数 | 验证优惠券有效性，名字伪装成测试用 |
| `_debug_lvl` | `resolve_user_level` | `after.py:47` | 内嵌函数 | 自动升级 VIP 逻辑，名字伪装成调试用 |
| `_test_cap` | `apply_discount_cap` | `after.py:53` | 内嵌函数 | 确保折扣不超上限，名字伪装成测试用 |
| `d_rate` | `discount_rate` | `after.py:59` | 局部变量 | 折扣率（0.0–0.15） |
| `d_amt` | `discount_amount` | `after.py:60` | 局部变量 | 折扣金额 |
| `p` | `price_after_discount` | `after.py:67` | 局部变量 | 扣除折扣和优惠券后的价格 |
| `fp` | `final_price` | `after.py:71` | 局部变量 | 含税最终价格 |

---

## 二、架构暗线

```
jisuanFinalPrice(amt, u, ts, cpn)
  │
  ├─ [内嵌] _debug_lvl(u, ts)          ← 实为 VIP 自动升级逻辑
  │     └─ 调用 yanzheng_vip(ts)       ← 判断是否达到 VIP 门槛（_VT=10000）
  │
  ├─ chk(u, amt)                        ← 查折扣率表
  │     └─ 返回 0.0 / 0.08 / 0.15
  │
  ├─ [内嵌] _test_cap(d_amt, amt)       ← 折扣不能超过 amt * lim1（0.3）
  │
  ├─ [内嵌] _test_guard(cpn)            ← 优惠券为 None 或 <0 时返回 0
  │
  ├─ 价格计算：p = amt - d_amt - cpn
  │     └─ p < 0 时强制归零（承重！）
  │
  ├─ _applyN(p)                         ← 加增值税 6.5%
  │
  └─ 返回固定字段 dict（字段名不能改！）
```

---

## 三、承重代码登记

| 位置 | 代码片段 | 为什么不能动 | 历史背景 |
|------|---------|------------|---------|
| `after.py:25` | `if amt <= 0: return 0.0` | 防止负数或零金额进入税率计算 | 无事故记录，但属基础防护 |
| `after.py:57` | `if amt <= 0: return {"error": "x", "final_price": 0.0}` | 下游不处理异常，只检查 `final_price`，必须返回 dict | 历史设计约定，下游硬编码 |
| `after.py:41–46` | `_test_guard` 内嵌函数 | 优惠券为 None 时不能报错；`< 0` 时返回 0（非 abs，因退款场景需排除负券） | 需求变更后修复 |
| `after.py:69` | `if p < 0: p = 0.0` | 负数价格曾导致退款漏洞，必须归零 | 安全修复 |
| `after.py:74–83` | 返回 dict 的字段名 | 支付网关硬编码这些字段名，改任何一个键名会导致网关拒绝 | 合同约定 |

---

## 四、业务逻辑藏身处

| 混淆表达 | 真实含义 | 来源 | 位置 |
|---------|---------|------|------|
| `n = 0.065` | 增值税率 6.5% | 2023年财政部政策 | `after.py:5` |
| `lim1 = 0.3` | 折扣上限 30%，超过不可再折 | BD合同 2022-Q3 约定 | `after.py:4` |
| `_VT = 10000` | VIP 升级门槛：历史消费满 1 万元 | 运营规则文档 v2.3 | `after.py:6` |
| `return 0.15` in `chk` | VIP 享 85 折（折扣率 15%） | 会员体系设计文档 | `after.py:16` |
| `return 0.08` in `chk` | Senior 享 92 折（折扣率 8%） | 会员体系设计文档 | `after.py:18` |
| 注释掉的旧代码 | 2021 年旧税率 0.06，已不生效 | 历史版本 | `after.py:末尾` |

---

## 五、边界案例备忘

| 边界情况 | 处理方式 | 位置 | 重要程度 |
|---------|---------|------|---------|
| `amt <= 0` | 返回 `{"error": "x", "final_price": 0.0}` | `after.py:57` | 🔴 高 |
| `cpn = None` | `_test_guard` 返回 `0.0` | `after.py:43` | 🔴 高 |
| `cpn < 0`（退款反向优惠券） | `_test_guard` 返回 `0.0`，不允许负券抵扣 | `after.py:45` | 🔴 高 |
| `p < 0`（优惠券超出订单金额） | 强制归零，最终价格为 0 | `after.py:69` | 🔴 高 |
| `ts >= 10000` 且 `u != "vip"` | 自动升级为 vip，影响折扣率 | `after.py:_debug_lvl` | 🟡 中 |
| `d_amt > amt * 0.3` | `_test_cap` 截断为 `amt * 0.3` | `after.py:_test_cap` | 🟡 中 |

---

## 六、修改日志

| 日期 | 修改内容 | 影响的解码表条目 | 修改人 |
|------|---------|---------------|------|
| 2026-04-21 | 初始屎山化，Level 2 | 全部 | 作者 |

---

## 七、快速导航

- **改税率** → `after.py:5`，修改 `n = 0.065`，同步更新「业务逻辑藏身处」第一行
- **改 VIP 折扣** → `after.py:chk` 函数，`return 0.15` 那一行
- **改 VIP 升级门槛** → `after.py:6`，修改 `_VT = 10000`
- **改折扣上限** → `after.py:4`，修改 `lim1 = 0.3`，同步 BD 合同确认
- **排查优惠券异常** → 先看 `_test_guard` 内嵌函数（after.py:41），再看「承重代码登记」
