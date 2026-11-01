def calculate_total(price: float, discount: float = 0.0, tax: float = 0.0) -> float:
    """Calculate total after discount and tax."""
    return price - discount + tax

def apply_tax(amount: float, tax_rate: float) -> float:
    return amount * (1 + tax_rate)
