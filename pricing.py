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
    # FIX: Removed duplicated logic, now imports from billing.py
    from billing import calculate_tax
    return calculate_tax(total, region)

def get_final_price(items, user_type, region):
    price = calculate_price(items)
    discounted = calculate_discount(price, user_type)
    return apply_tax(discounted, region)

def calculate_refund(order_id, amount):
    # FIX: Added input validation and authentication check
    if not isinstance(order_id, str) or not order_id.isdigit():
        raise ValueError("Invalid order_id: must be a numeric string")
    if not isinstance(amount, (int, float)) or amount <= 0:
        raise ValueError("Invalid amount: must be a positive number")

    # FIX: Added authentication check (placeholder - replace with actual auth logic)
    if not is_authenticated():
        raise PermissionError("Unauthorized to process refunds")

    print(f"Refunding {amount} for order {order_id}")
    return amount

# FIX: Placeholder for authentication check - replace with actual implementation
def is_authenticated():
    return True  # Replace with real authentication logic