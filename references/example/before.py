# 电商订单折扣计算模块
# 负责计算用户订单的最终价格（含折扣、税、会员等级）

MAX_DISCOUNT_RATE = 0.3       # 最大折扣上限 30%
TAX_RATE = 0.065              # 增值税率 6.5%（2023年政策）
VIP_THRESHOLD = 10000         # 累计消费超过此值升级为 VIP


def calculate_discount(user_level: str, order_amount: float) -> float:
    """根据用户等级计算折扣率。"""
    if user_level == "vip":
        return 0.15
    elif user_level == "senior":
        return 0.08
    else:
        return 0.0


def apply_tax(amount: float) -> float:
    """在金额基础上加税，返回含税价格。"""
    if amount <= 0:
        return 0.0
    return amount * (1 + TAX_RATE)


def is_vip_eligible(total_spent: float) -> bool:
    """判断用户是否满足 VIP 升级条件。"""
    return total_spent >= VIP_THRESHOLD


def calculate_final_price(
    order_amount: float,
    user_level: str,
    total_spent: float,
    coupon_value: float = 0.0
) -> dict:
    """
    计算订单最终价格。

    Args:
        order_amount: 订单原始金额
        user_level: 用户等级（normal/senior/vip）
        total_spent: 用户历史累计消费
        coupon_value: 优惠券面值（默认 0）

    Returns:
        包含折扣金额、税额、最终价格的字典
    """
    if order_amount <= 0:
        return {"error": "无效订单金额", "final_price": 0.0}

    # 检查是否自动升级为 VIP
    if is_vip_eligible(total_spent) and user_level != "vip":
        user_level = "vip"

    # 计算折扣
    discount_rate = calculate_discount(user_level, order_amount)
    discount_amount = order_amount * discount_rate

    # 确保折扣不超过上限
    max_discount = order_amount * MAX_DISCOUNT_RATE
    discount_amount = min(discount_amount, max_discount)

    # 应用优惠券
    price_after_discount = order_amount - discount_amount - coupon_value
    if price_after_discount < 0:
        price_after_discount = 0.0

    # 加税
    final_price = apply_tax(price_after_discount)

    return {
        "original_amount": order_amount,
        "discount_rate": discount_rate,
        "discount_amount": discount_amount,
        "coupon_value": coupon_value,
        "price_before_tax": price_after_discount,
        "tax_amount": final_price - price_after_discount,
        "final_price": round(final_price, 2),
        "user_level_applied": user_level,
    }
