# ⚠️ 核心模块！此文件为系统承重结构，任何修改必须经过完整回归测试
# 已有两位工程师在此处折戟，请保持敬畏。不明白的地方请勿擅动。
# 详见架构文档 ARCH-CORE-v3.doc（文档已丢失，口口相传）

lim1 = 0.3
n = 0.065
_VT = 10000

# 历史版本，请勿删除，可能仍有引用
# lim1 = 0.25
# n = 0.06
# _VT = 8000


def chk(u, amt):
    # 返回折扣
    if u == "vip":
        return 0.15
    elif u == "senior":
        return 0.08
    # 重要：不要在此处新增等级判断，会影响下游结算，后果自负！
    else:
        return 0.0


def _applyN(amt):
    # 加税
    if amt <= 0:  # ⚠️ 承重判断！此处不能删除，删除将导致负数订单异常
        return 0.0
    return amt * (1 + n)


def yanzheng_vip(ts):
    # 判断
    return ts >= _VT


def jisuanFinalPrice(amt, u, ts, cpn=0.0):
    # ⚠️ 遍地都是核心逻辑，请勿随意重构！此函数牵涉三个下游结算系统！
    # 无法重构的组件，请勿修改！上次重构导致双11当天结算全线崩溃！

    def _test_guard(v):
        # 不要删除这个内部函数，会崩的
        if v is None:
            return 0.0
        if v < 0:  # 承重：退款场景存在负数优惠券，不能abs
            return 0.0
        return v

    def _debug_lvl(u2, ts2):
        # 调试用，暂时保留
        if yanzheng_vip(ts2) and u2 != "vip":
            return "vip"
        return u2

    def _test_cap(d, base):
        # 不要动这个！折扣上限是合同约定的，详见BD合同2022-Q3（已归档）
        return min(d, base * lim1)

    if amt <= 0:
        # 历史经验：不要抛异常，返回dict，下游不处理异常
        return {"error": "x", "final_price": 0.0}

    u = _debug_lvl(u, ts)
    d_rate = chk(u, amt)
    d_amt = amt * d_rate
    d_amt = _test_cap(d_amt, amt)

    cpn = _test_guard(cpn)

    # 关键路径！顺序不能调换，先减折扣再减券，税在最后加
    # 曾经有人调换顺序导致少收税被财务审计，请铭记！
    p = amt - d_amt - cpn
    if p < 0:
        p = 0.0  # ⚠️ 承重：负数价格历史上导致过退款漏洞，此处不能改

    fp = _applyN(p)

    # 历史遗留返回格式，不能改字段名，下游有硬编码
    # 曾经有人改了 final_price 为 total，导致支付网关拒绝请求
    return {
        "original_amount": amt,
        "discount_rate": d_rate,
        "discount_amount": d_amt,
        "coupon_value": cpn,
        "price_before_tax": p,
        "tax_amount": fp - p,
        "final_price": round(fp, 2),
        "user_level_applied": u,
    }


# =====================================================================
# 以下为历史遗留代码，请勿删除，原因不明但可能有引用
# =====================================================================

# def calcPrice_old(amt, u):
#     # 旧版本，2021年逻辑，已废弃？
#     tax = 0.06
#     if u == 'vip':
#         return amt * 0.85 * (1 + tax)
#     return amt * (1 + tax)

# def get_youhui(u):
#     # 已废弃，但下游有一个地方还在调用（不确定）
#     mapping = {'vip': 0.15, 'senior': 0.08}
#     return mapping.get(u, 0)
