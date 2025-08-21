import streamlit as st, json
from pathlib import Path
from src.engine.planner import get_destination_doc, build_itinerary, default_assumptions
from src.engine.budget import estimate_budget
from src.core.structured_output import TripPlan, DayPlan, Budget, human_summary
from src.functions.weather import get_weather

def load_corpus() -> list:
    return json.loads(Path("data/travel_facts.json").read_text(encoding="utf-8"))

st.title("TripMitra – AI Travel Planner (Local Demo)")
col1, col2 = st.columns(2)
with col1:
    destination = st.text_input("Destination", "Bali")
    days = st.number_input("Days", 1, 21, 5, 1)
with col2:
    tier = st.selectbox("Budget Tier", ["budget","mid","premium"], 1)
    budget_cap = st.number_input("Budget Cap (optional)", 0, 100000, 1000, 50)

interests = st.multiselect("Interests", ["beaches","culture","adventure","food","museums","temples","markets"],
                           default=["beaches","culture","adventure"])

if st.button("Plan my trip"):
    corpus = load_corpus()
    doc = get_destination_doc(destination, corpus) or {}
    it = build_itinerary(destination, int(days), interests, doc)
    acc, food, trans, acts = estimate_budget(int(days), tier, float(budget_cap))
    assumptions = default_assumptions(float(budget_cap))
    if doc.get("best_time"):
        assumptions.append(f"Best time (from RAG): {doc['best_time']}")
    assumptions.append(f"Weather hint: {get_weather(destination, 'any')}")

    itinerary = [DayPlan(day=i+1, activity=it[i]) for i in range(int(days))]
    plan = TripPlan(destination=destination, duration_days=int(days), assumptions=assumptions,
                    itinerary=itinerary, budget=Budget(accommodation=acc, food=food, transport=trans, activities=acts))

    st.subheader("Human-Friendly Plan")
    st.text(human_summary(plan))
    st.subheader("Structured JSON")
    st.json(plan.to_json())
