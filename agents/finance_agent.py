from strands import Agent, tool
from strands.models.gemini import GeminiModel

from tools.finance_tools import (
    analyze_transactions,
    spending_by_category,
    detect_unusual_transactions,
    financial_health_score,
    generate_recommendations
)


# Current transaction file used by the agent
FILE_PATH = "data/transactions.csv"


def set_file_path(file_path):
    global FILE_PATH
    FILE_PATH = file_path


@tool
def analyze_finances():
    """Analyze income, expenses, savings, and transaction count."""
    return analyze_transactions(FILE_PATH)


@tool
def get_spending_categories():
    """Analyze spending by expense category."""
    return spending_by_category(FILE_PATH)


@tool
def find_unusual_transactions():
    """Find unusually large expenses."""
    return detect_unusual_transactions(FILE_PATH)


@tool
def get_financial_health():
    """Calculate financial health score and savings rate."""
    return financial_health_score(FILE_PATH)


@tool
def get_recommendations():
    """Generate personalized financial recommendations."""
    return generate_recommendations(FILE_PATH)


model = GeminiModel(
    model_id="gemini-3.6-flash"
)


agent = Agent(
    model=model,

    system_prompt="""
You are FinAgent, an autonomous personal finance assistant.

Your job is to understand the user's financial question and
autonomously decide which finance tools are necessary.

Do not automatically use every tool.

Choose only the tools required to answer the user's request.

Examples:
- Spending questions → use spending category analysis.
- Unusual transaction questions → use unusual transaction detection.
- Financial health questions → use financial health analysis.
- General financial analysis → use multiple relevant tools.
- Recommendation questions → use financial health and spending tools
  when necessary.

Always base financial numbers on tool results.
Never invent financial numbers.

All amounts are in Indian Rupees (INR).
Always use the ₹ symbol when presenting financial amounts.
Never use $, USD, or dollars.

Give clear, concise and actionable financial insights.
""",

    tools=[
        analyze_finances,
        get_spending_categories,
        find_unusual_transactions,
        get_financial_health,
        get_recommendations
    ]
)