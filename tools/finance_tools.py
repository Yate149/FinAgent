import pandas as pd


def analyze_transactions(file_path):
    df = pd.read_csv(file_path)

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expenses = df[df["Type"] == "Expense"]["Amount"].sum()

    savings = income - expenses

    return {
        "total_income": income,
        "total_expenses": expenses,
        "savings": savings,
        "transaction_count": len(df)
    }


def categorize_expense(description):
    description = description.lower()

    if "restaurant" in description:
        return "Food"
    elif "grocery" in description:
        return "Groceries"
    elif "amazon" in description:
        return "Shopping"
    elif "uber" in description:
        return "Transportation"
    elif "electricity" in description:
        return "Utilities"
    elif "netflix" in description:
        return "Entertainment"
    elif "rent" in description:
        return "Housing"
    else:
        return "Other"


def categorize_transactions(file_path):
    df = pd.read_csv(file_path)

    expenses = df[df["Type"] == "Expense"].copy()

    expenses["Category"] = expenses["Description"].apply(
        categorize_expense
    )

    return expenses[
        ["Date", "Description", "Amount", "Category"]
    ].to_dict(orient="records")
def spending_by_category(file_path):
    df = pd.read_csv(file_path)

    expenses = df[df["Type"] == "Expense"].copy()

    expenses["Category"] = expenses["Description"].apply(
        categorize_expense
    )

    category_totals = (
        expenses.groupby("Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    return category_totals.to_dict()
def detect_unusual_transactions(file_path):
    df = pd.read_csv(file_path)

    expenses = df[df["Type"] == "Expense"].copy()

    average_expense = expenses["Amount"].mean()
    threshold = average_expense * 2

    unusual = expenses[
        expenses["Amount"] > threshold
    ].copy()

    return unusual[
        ["Date", "Description", "Amount"]
    ].to_dict(orient="records")
def calculate_savings_rate(file_path):
    df = pd.read_csv(file_path)

    income = df[df["Type"] == "Income"]["Amount"].sum()
    expenses = df[df["Type"] == "Expense"]["Amount"].sum()

    savings = income - expenses

    if income == 0:
        return 0

    savings_rate = (savings / income) * 100

    return round(savings_rate, 2)
def financial_health_score(file_path):
    savings_rate = calculate_savings_rate(file_path)

    if savings_rate >= 30:
        score = 90
        status = "Excellent"
    elif savings_rate >= 20:
        score = 75
        status = "Good"
    elif savings_rate >= 10:
        score = 60
        status = "Moderate"
    else:
        score = 40
        status = "Needs Improvement"

    return {
        "score": score,
        "status": status,
        "savings_rate": savings_rate
    }
def generate_recommendations(file_path):
    health = financial_health_score(file_path)
    spending = spending_by_category(file_path)

    recommendations = []

    if health["savings_rate"] < 20:
        recommendations.append(
            "Try to increase your savings rate to at least 20%."
        )
    else:
        recommendations.append(
            "Your savings rate is healthy. Continue maintaining it."
        )

    if spending.get("Food", 0) > 3000:
        recommendations.append(
            "Food spending is relatively high. Consider setting a monthly food budget."
        )

    if spending.get("Shopping", 0) > 2000:
        recommendations.append(
            "Shopping expenses are significant. Review non-essential purchases."
        )

    if spending.get("Entertainment", 0) > 1000:
        recommendations.append(
            "Consider reducing discretionary entertainment spending."
        )

    return recommendations