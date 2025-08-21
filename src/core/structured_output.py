from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class DayPlan:
    day: int
    activity: str

@dataclass
class Budget:
    accommodation: float
    food: float
    transport: float
    activities: float
    def total(self) -> float:
        return round(self.accommodation + self.food + self.transport + self.activities, 2)

@dataclass
class TripPlan:
    destination: str
    duration_days: int
    assumptions: List[str]
    itinerary: List[DayPlan]
    budget: Budget
    def to_json(self) -> Dict[str, Any]:
        d = asdict(self)
        d["budget"]["total"] = self.budget.total()
        return d

def human_summary(plan: TripPlan) -> str:
    lines = []
    lines.append(f"🎒 TripMitra Plan: {plan.destination} ({plan.duration_days} days)")
    if plan.assumptions:
        lines.append("Assumptions: " + "; ".join(plan.assumptions))
    lines.append("\nItinerary:")
    for dp in plan.itinerary:
        lines.append(f"  Day {dp.day}: {dp.activity}")
    b = plan.budget
    lines.append("\nBudget (est.):")
    lines.append(f"  Accommodation: {b.accommodation:.0f}")
    lines.append(f"  Food: {b.food:.0f}")
    lines.append(f"  Transport: {b.transport:.0f}")
    lines.append(f"  Activities: {b.activities:.0f}")
    lines.append(f"  Total: {b.total():.0f}")
    return "\n".join(lines)
