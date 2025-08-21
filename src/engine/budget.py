from typing import Tuple
def estimate_budget(days: int, city_category: str = "mid", budget_cap: float = 0.0) -> Tuple[float,float,float,float]:
    tiers = {
        "budget":   (25, 15, 8, 12),
        "mid":      (60, 30, 12, 25),
        "premium":  (120, 60, 20, 50)
    }
    if city_category not in tiers:
        city_category = "mid"
    a, f, t, act = tiers[city_category]
    acc = a * days
    food = f * days
    trans = t * days
    activities = act * days * 0.5
    total = acc + food + trans + activities
    if budget_cap and total > budget_cap:
        scale = budget_cap / total
        acc, food, trans, activities = acc*scale, food*scale, trans*scale, activities*scale
    return round(acc,2), round(food,2), round(trans,2), round(activities,2)
