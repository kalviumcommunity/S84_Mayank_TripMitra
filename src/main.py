import json, argparse
from engine.planner import get_destination_doc, build_itinerary, default_assumptions
from engine.budget import estimate_budget
from engine.flights import get_flight_details
from core.structured_output import TripPlan, DayPlan, Budget, human_summary
from functions.weather import get_weather
from pathlib import Path

# Simple currency conversion stub (replace with real API if needed)
def get_currency_rate(from_currency: str, to_currency: str) -> float:
    # Example: USD to INR fixed rate
    if from_currency == "USD" and to_currency == "INR":
        return 83.0
    return 1.0

def load_corpus():
    base = Path(__file__).resolve().parent.parent  # project root
    path = base / "data" / "travel_facts.json"
    return json.loads(path.read_text(encoding="utf-8"))


def plan_trip(destination: str, days: int, interests: list, budget_cap: float = 0.0, tier: str = "mid"):
    corpus = load_corpus()
    doc = get_destination_doc(destination, corpus) or {}
    it_list = build_itinerary(destination, days, interests, doc)
    acc, food, trans, acts = estimate_budget(days, tier, budget_cap)
    assumptions = default_assumptions(budget_cap)

    # Add destination-specific assumptions
    if doc.get("best_time"):
        assumptions.append(f"Best time (from RAG): {doc['best_time']}")
    assumptions.append(f"Weather hint: {get_weather(destination, 'any')}")

    # ---- Currency Conversion (USD → INR) ----
    rate = get_currency_rate("USD", "INR")
    acc, food, trans, acts = [round(x * rate, 2) for x in (acc, food, trans, acts)]

    itinerary = [DayPlan(day=i+1, activity=it_list[i]) for i in range(days)]
    plan = TripPlan(
        destination=destination,
        duration_days=days,
        assumptions=assumptions,
        itinerary=itinerary,
        budget=Budget(
            accommodation=acc,
            food=food,
            transport=trans,
            activities=acts
        )
    )
    return plan, "INR"   # also return currency


def main():
    ap = argparse.ArgumentParser(description="TripMitra – Local demo (no external APIs).")
    ap.add_argument("--destination", required=True)
    ap.add_argument("--days", type=int, required=True)
    ap.add_argument("--interests", nargs="*", default=["culture","food"])
    ap.add_argument("--budget_cap", type=float, default=0.0)
    ap.add_argument("--tier", choices=["budget","mid","premium"], default="mid")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    plan, currency = plan_trip(args.destination, args.days, args.interests, args.budget_cap, args.tier)

    print("=== Human Summary ===\n")
    print(human_summary(plan))
    print(f"\n=== Structured JSON (currency: {currency}) ===")

    js = plan.to_json()
    js["currency"] = currency   # add currency info in JSON

    print(json.dumps(js, indent=2, ensure_ascii=False))
    if args.out:
        Path(args.out).write_text(json.dumps(js, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nSaved JSON to {args.out}")


if __name__ == "__main__":
    main()