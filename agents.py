# agents.py

import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, LLM

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ==============================
# LLM
# ==============================

llm = LLM(
    model="groq/llama-3.1-8b-instant",
    temperature=0.2, 
    top_p=0.7,
    max_tokens=1200
)

# ==============================
# Agents
# ==============================

financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and produce structured summaries.",
    backstory=(
        "You are an experienced financial analyst specializing in "
        "financial statement analysis, valuation, and risk evaluation. "
        "You rely strictly on verified financial data and avoid speculation."
    ),    
    llm=llm,
    verbose=False,
    memory=False,
    max_iter=2,
)

investment_advisor = Agent(
    role="Investment Advisor",
    goal="Provide investment recommendations from financial summaries.",
    backstory=(
        "You are a professional investment advisor who provides balanced "
        "Buy/Hold/Sell opinions supported by financial evidence."
    ),
    llm=llm,
    verbose=False,
    memory=False,
    max_iter=2,
)

risk_assessor = Agent(
    role="Risk Specialist",
    goal="Identify financial and market risks from summaries.",
    backstory=(
        "You specialize in identifying downside risks, liquidity concerns, "
        "and sustainability of company performance."
    ),    
    llm=llm,
    verbose=False,
    memory=False,
    max_iter=2,
)