def get_currency_rate(base: str, target: str) -> float:
    sample = {
        ("USD","INR"): 83.0,
        ("EUR","INR"): 90.0,
        ("USD","EUR"): 0.92
    }
    return sample.get((base.upper(), target.upper()), 1.0)
