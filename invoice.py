from calculator import calculate_total


def generate_invoice(order_id, price, discount):
    total = calculate_total(price, discount)
    return {"order_id": order_id, "total": total}
