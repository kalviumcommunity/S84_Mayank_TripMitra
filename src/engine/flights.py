def get_flight_details(destination: str, tier: str = "mid") -> dict:
    # Sample static flight costs in USD
    sample_flights = {
        "Paris": {"from": "Delhi", "price_usd": {"budget": 500, "mid": 800, "premium": 1500}},
        "Bali": {"from": "Delhi", "price_usd": {"budget": 400, "mid": 700, "premium": 1200}},
        "New York": {"from": "Delhi", "price_usd": {"budget": 700, "mid": 1100, "premium": 2000}}
    }

    if destination not in sample_flights:
        return {
            "from": "Delhi",
            "to": destination,
            "airline": "Generic Airlines",
            "price_usd": 600,
            "notes": "Estimated price (no data found for this destination)"
        }

    data = sample_flights[destination]
    return {
        "from": data["from"],
        "to": destination,
        "airline": "Sample Airlines",
        "price_usd": data["price_usd"][tier]
    }
