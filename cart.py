from calculator import calculate_total


def checkout(items, discount_code=None):
    total = 0
    for item in items:
        discount = item.get("discount", 0) if discount_code else 0
        total += calculate_total(item["price"], discount)
    return total


def cart_summary(cart_items):
    subtotal = sum(
        calculate_total(item["price"], item.get("discount", 0))
        for item in cart_items
    )
    return {"subtotal": subtotal, "tax": 0}
