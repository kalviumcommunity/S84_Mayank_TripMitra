from typing import List, Dict
from .utils import match_score

def get_destination_doc(destination: str, corpus: List[Dict]) -> Dict:
    dest = destination.strip().lower()
    best, best_score = None, -1
    for doc in corpus:
        s = match_score(dest, doc.get("destination",""))
        if s > best_score:
            best, best_score = doc, s
    return best or {}

def build_itinerary(destination: str, days: int, interests: List[str], doc: Dict) -> List[str]:
    attractions = doc.get("top_attractions", [])
    plan = []
    i = 0
    while len(plan) < days:
        if i < len(attractions):
            plan.append(attractions[i])
        else:
            plan.append(f"Explore local neighborhoods & markets in {destination}")
        i += 1
    # Interest nudges
    for idx, activity in enumerate(plan):
        for intr in (interests or []):
            low = intr.lower()
            if low in ["beach","beaches"] and "beach" not in activity.lower():
                plan[idx] = activity + " + Relax at a nearby beach"
                break
            if low in ["culture","temples","museums"] and "temple" not in activity.lower() and "museum" not in activity.lower():
                plan[idx] = activity + " + Cultural stop (temple/museum)"
                break
            if low in ["adventure","water sports"] and "water" not in activity.lower():
                plan[idx] = activity + " + Try an adventure activity"
                break
    return plan

def default_assumptions(budget_cap: float) -> List[str]:
    a = ["Mid-range stays unless specified", "Public transport / rideshare", "Two paid activities overall"]
    if budget_cap:
        a.append(f"Stay within budget cap ≈ {budget_cap:.0f}")
    return a
