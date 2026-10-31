from calculator import calculate_total


def test_calculate_total_basic():
    assert calculate_total(100, 10) == 90


def test_calculate_total_no_discount():
    assert calculate_total(50, 0) == 50
