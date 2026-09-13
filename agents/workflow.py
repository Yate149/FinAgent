from agents.finance_agent import agent


def run_financial_analysis():

    prompt = """
    Analyze the user's financial data.

    First determine which financial analyses are needed.
    Use the available tools to:
    - calculate income and expenses
    - calculate savings and savings rate
    - analyze spending categories
    - detect unusual transactions
    - assess financial health
    - generate recommendations

    Then provide a concise financial health report.
    """

    response = agent(prompt)

    return response