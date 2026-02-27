# task.py

from crewai import Task
from agents import (
    financial_analyst,
    investment_advisor,
    risk_assessor
)

# ==============================
# Financial Summary
# ==============================

financial_summary = Task(
    description=(
        "You are given a financial document below:\n\n"
        "{document_text}\n\n"
        "Answer the user query: {query}.\n\n"
        "IMPORTANT RULES:\n"
        "- Use ONLY information present in the document_text.\n"
        "- Do NOT invent financial numbers.\n"
        "- If data is missing, say 'Not explicitly stated'.\n"
        "- Support conclusions using document evidence."
    ),
    expected_output=(
        "Structured financial analysis including:\n"
        "- Revenue trend summary\n"
        "- Profitability analysis\n"
        "- Cash flow evaluation\n"
        "- Balance sheet strength\n"
        "- Key operational highlights"
    ),
    agent=financial_analyst,
)

# ==============================
# Investment Recommendation
# ==============================

investment_analysis = Task(
    description=(
        "Identify risks explicitly mentioned or logically inferred "
        "from the document_text and prior analysis.\n"
        "Do NOT fabricate risks or numbers."
    ),
    expected_output=(
        "Investment recommendation including:\n"
        "- Buy/Hold/Sell decision\n"
        "- Supporting financial metrics\n"
        "- Long-term outlook"
    ),
    agent=investment_advisor,
)

# ==============================
# Risk Assessment
# ==============================

risk_assessment = Task(
    description=(
        "Identify financial and operational risks present in the financial document. "
        "Focus on liquidity risks, margin pressure, macroeconomic exposure, "
        "and operational uncertainties."
    ),
    expected_output=(
        "Final report combining:\n"
        "- Financial summary\n"
        "- Investment recommendation\n"
        "- Risk assessment\n"
        "Provide a complete investor-ready analysis."
    ),
    agent=risk_assessor,
)