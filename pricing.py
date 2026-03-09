"""Pricing calculation module."""

def calculate_price(items):
    total = 0
    for item in items:
        if item['type'] == 'basic':
            total += item['quantity'] * 9.99
        elif item['type'] == 'pro':
            total += item['quantity'] * 19.99
        elif item['type'] == 'enterprise':
            total += item['quantity'] * 49.99
    return total

def calculate_discount(total, user_type):
    if user_type == 'premium':
        discount = total * 0.1
    elif user_type == 'vip':
        discount = total * 0.2
    else:
        discount = 0
    return total - discount

def apply_tax(total, region):
    # Duplicated logic from billing.py
    if region == 'US':
        return total * 1.08
    elif region == 'EU':
        return total * 1.20
    else:
        return total

def get_final_price(items, user_type, region):
    price = calculate_price(items)
    discounted = calculate_discount(price, user_type)
    return apply_tax(discounted, region)

def calculate_refund(order_id, amount):
    # No validation, no auth check
    print(f"Refunding {amount} for order {order_id}")
    return amount
