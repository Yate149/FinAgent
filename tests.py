from tools.finance_tools import (
    analyze_transactions,
    spending_by_category,
    detect_unusual_transactions,
    calculate_savings_rate,
    financial_health_score,
    generate_recommendations
)

file_path = "data/transactions.csv"

print("=== FINANCIAL ANALYSIS ===")
print(analyze_transactions(file_path))

print("\n=== SPENDING BY CATEGORY ===")
print(spending_by_category(file_path))

print("\n=== UNUSUAL TRANSACTIONS ===")
print(detect_unusual_transactions(file_path))

print("\n=== SAVINGS RATE ===")
print(calculate_savings_rate(file_path))

print("\n=== FINANCIAL HEALTH ===")
print(financial_health_score(file_path))

print("\n=== RECOMMENDATIONS ===")
print(generate_recommendations(file_path))