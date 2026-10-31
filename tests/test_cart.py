from cart import cart_summary


def test_cart_summary_empty_cart():
    assert cart_summary([]) == {"subtotal": 0, "tax": 0}
