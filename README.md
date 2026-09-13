# FinAgent

## AI-Powered Personal Finance Assistant

FinAgent is an autonomous AI-powered personal finance assistant built using the Strands Agents SDK and Gemini. It analyzes transaction data, identifies spending patterns, detects unusual transactions, evaluates financial health, and provides personalized financial recommendations.

## Problem

Managing personal finances often requires manually reviewing transactions, calculating expenses, identifying unnecessary spending, and monitoring savings. This can be time-consuming and difficult for users who are not financially experienced.

## Solution

FinAgent automates this process. Users can upload their transaction CSV, and the agent can autonomously decide which financial analysis tools are required to answer questions and generate useful financial insights.

## Key Features

- Upload transaction data through a CSV file
- Analyze total income and expenses
- Calculate savings and savings rate
- Categorize expenses
- Identify unusual transactions
- Calculate financial health score
- Generate personalized recommendations
- Ask natural-language questions about finances
- Autonomous tool selection using Strands Agents SDK
- Interactive Streamlit dashboard

## Agentic Workflow

The user provides financial data or asks a financial question.

FinAgent analyzes the request and decides which specialized finance tools are required.

Available tools include:

1. Transaction Analysis
2. Spending Category Analysis
3. Unusual Transaction Detection
4. Financial Health Assessment
5. Recommendation Generation

The selected tools analyze the transaction data and return results to the agent, which then generates a concise financial response.

## Technology Stack

- Python
- Strands Agents SDK
- Gemini
- Streamlit
- Pandas

## Project Structure

```text
FinAgent/
├── agents/
│   ├── finance_agent.py
│   └── workflow.py
│
├── tools/
│   └── finance_tools.py
│
├── data/
│   └── transactions.csv
│
├── app.py
├── tests.py
└── README.md