from agents.finance_agent import agent, set_file_path


response = agent(
    "Analyze my finances. Tell me my income, expenses, "
    "savings, savings rate, unusual transactions, "
    "financial health, and recommendations."
)

print(response)