🧳 TripMitra – AI Travel Planner

TripMitra is an AI-powered travel planning assistant that helps users generate personalized trip itineraries based on their destination, number of days, interests, budget, and travel tier (basic, premium, luxury). The project demonstrates multiple prompt engineering techniques and LLM concepts such as system & user prompts, zero/one/multi-shot prompting, dynamic prompting, chain of thought, structured outputs, function calling, evaluation pipeline, and LLM parameters (temperature, top-p, top-k, stop sequences, tokenization).

🚀 Project Idea

Planning a trip is stressful — finding flights, budgeting, and creating an itinerary. TripMitra solves this by:

Taking user inputs (destination, days, interests, budget, tier)

Generating daily itineraries with places to visit, activities, and food options

Including budget breakdowns in INR (flights, hotels, activities, food)

Outputting results in both human-friendly summaries and structured JSON for further use in applications.

⚙️ Implementation (Technical)

Backend: Python with OpenAI LLM API

Prompts: Custom designed with RTFC framework (Role, Task, Format, Constraints)

Outputs: JSON + readable text

Advanced Techniques: Function Calling, Structured Output, Stop Sequences

Evaluation: Automated pipeline with judge prompts

📜 Prompt Engineering Techniques
1️⃣ System and User Prompt

System Prompt defines the role: “You are TripMitra, an AI-powered travel planner that creates itineraries, budgets, and includes flights in INR.”

User Prompt example: “Plan a 4-day premium trip to Mumbai with museums, food, culture, and a budget cap of ₹20,000 including flight details.”

📌 RTFC Framework Used:

R (Role): Trip planner

T (Task): Generate itinerary + budget + flights

F (Format): Human summary + JSON

C (Constraints): INR, budget cap, tier type

2️⃣ Zero Shot Prompting

Prompt Example:
“Plan a 3-day trip to Jaipur for a budget of ₹10,000. Include hotel, food, and sightseeing details.”

Explanation in video: Zero-shot means no examples are given, model must figure out directly from instructions.

3️⃣ One Shot Prompting

Prompt Example:
“Here is an example of a 2-day trip to Goa: [Example JSON]. Now plan a 3-day trip to Manali with a budget of ₹15,000.”

Explanation in video: One-shot means we give one example for the model to learn format/style.

4️⃣ Multi Shot Prompting

Prompt Example:
“Example 1: 2-day Goa trip… Example 2: 3-day Delhi trip… Now generate a 4-day Kerala trip.”

Explanation in video: Multi-shot means giving multiple examples so the model generalizes better.

5️⃣ Dynamic Prompting

Implementation: Take real user input from CLI → inject into prompt.

Example: python main.py --destination Mumbai --days 4 --interests "food culture" --budget 20000 --tier premium

Explanation in video: Dynamic prompting adapts prompts at runtime.

6️⃣ Chain of Thought Prompting

Prompt Example:
“Think step by step: First calculate daily budget, then assign flights, hotels, food, activities, finally summarize.”

Explanation in video: Forces the model to show reasoning before final answer.

🧪 Evaluation Dataset and Testing Framework

Dataset: At least 5 test cases (different cities, budgets, tiers).

Judge Prompt: “Does the AI output include itinerary, flights, budget breakdown in INR, and stay within budget?”

Framework: Python test script runs all cases → compares actual vs expected.

🔑 LLM Parameters Used

Tokens & Tokenization: Logged after each API call (print(response.usage.tokens))

Temperature: Controls randomness (e.g., 0.7 = more creative itineraries, 0.2 = strict outputs)

Top-P: Nucleus sampling to limit to most likely tokens

Top-K: Picks from top K probable tokens

Stop Sequence: Stops at </END> to prevent extra text

📦 Structured Output

Used JSON schema for itinerary & budget.

⚡ Function Calling

Implemented get_currency_rate() and fetch_flights() functions.

AI calls them when needed (e.g., converting USD → INR, fetching dummy flight data).
