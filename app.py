import streamlit as st

from agents.finance_agent import agent, set_file_path

from tools.finance_tools import (
    analyze_transactions,
    spending_by_category,
    detect_unusual_transactions,
    calculate_savings_rate,
    financial_health_score,
    generate_recommendations
)

st.set_page_config(
    page_title="FinAgent",
    page_icon="💰",
    layout="wide"
)

st.title("💰 FinAgent")
st.subheader("AI-Powered Personal Finance Assistant")

uploaded_file = st.file_uploader(
    "Upload your transaction CSV",
    type=["csv"]
)

if uploaded_file is not None:
    import tempfile

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".csv"
    ) as temp_file:
        temp_file.write(uploaded_file.getbuffer())
        FILE_PATH = temp_file.name
else:
    FILE_PATH = "data/transactions.csv"

set_file_path(FILE_PATH)

analysis = analyze_transactions(FILE_PATH)
categories = spending_by_category(FILE_PATH)
unusual = detect_unusual_transactions(FILE_PATH)
savings_rate = calculate_savings_rate(FILE_PATH)
health = financial_health_score(FILE_PATH)
recommendations = generate_recommendations(FILE_PATH)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Income", f"₹{analysis['total_income']:,}")
col2.metric("Total Expenses", f"₹{analysis['total_expenses']:,}")
col3.metric("Savings", f"₹{analysis['savings']:,}")
col4.metric("Savings Rate", f"{savings_rate}%")

st.divider()

st.header("Financial Health")

st.metric(
    "Health Score",
    f"{health['score']}/100",
    health["status"]
)

st.divider()

st.header("Spending by Category")

st.bar_chart(categories)

st.divider()

st.header("⚠️ Unusual Transactions")

if unusual:
    st.dataframe(unusual, use_container_width=True)
else:
    st.success("No unusual transactions detected.")
if unusual:
    st.warning(
        f"FinAgent detected {len(unusual)} unusual transaction(s) "
        "that may require your attention."
    )

st.divider()

st.header("💡 Recommendations")

for recommendation in recommendations:
    st.write("•", recommendation)
st.divider()

st.header("🤖 AI Financial Analyst")

if st.button("Generate AI Financial Report"):
    with st.spinner("FinAgent is analyzing your finances..."):
        response = agent(
            """
            Analyze the user's financial data and provide a concise
financial health report.

IMPORTANT:
- All financial amounts are in Indian Rupees (INR).
- Always display amounts using the ₹ symbol.
- Never use $, USD, or dollars.
- Use Indian financial terminology where appropriate.

            Use the available finance tools to analyze:
            - income and expenses
            - savings and savings rate
            - spending categories
            - unusual transactions
            - financial health
            - recommendations

            Present the results clearly and use the actual tool results.
            Do not invent financial numbers.
            """
        )

    st.markdown(str(response))
st.divider()

st.header("💬 Ask FinAgent")

user_question = st.text_input(
    "Ask a question about your finances"
)

if user_question:
    with st.spinner("FinAgent is thinking..."):
        response = agent(user_question)

    st.markdown(str(response))