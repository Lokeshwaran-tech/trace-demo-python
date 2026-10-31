from payment import process_payment


def test_process_payment_reports_amount():
    result = process_payment({"price": 100, "discount": 5, "card_token": "demo-token"})
    assert result["amount"] == 95
