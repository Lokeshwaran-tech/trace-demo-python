from calculator import calculate_total


def process_payment(order):
    amount = calculate_total(order["price"], order.get("discount", 0))
    return charge_card(order["card_token"], amount)


def charge_card(token, amount):
    return {"success": True, "amount": amount}
