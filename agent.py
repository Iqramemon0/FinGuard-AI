from strands import Agent, tool
from finance_analysis import analyze_finances


@tool
def analyze_financial_file() -> str:
    """
    Analyze the company's financial Excel file.
    Detect budget overruns and unusual transactions.
    """

    result = analyze_finances("data/financial_data.xlsx")

    report = []

    report.append("FINANCIAL SUMMARY")
    report.append(f"Total Budget: ${result['total_budget']:,.2f}")
    report.append(f"Actual Spending: ${result['total_actual']:,.2f}")
    report.append(f"Variance: ${result['total_variance']:,.2f}")
    report.append(f"Variance %: {result['variance_percent']:.2f}%")

    report.append("\nBUDGET OVERRUNS:")

    if result["budget_overruns"].empty:
        report.append("No budget overruns detected.")
    else:
        for _, row in result["budget_overruns"].iterrows():
            report.append(
                f"- {row['Department']}: "
                f"Budget ${row['Budget']:,.2f}, "
                f"Actual ${row['Actual']:,.2f}, "
                f"Overrun ${row['Variance']:,.2f}"
            )

    report.append("\nUNUSUAL TRANSACTIONS:")

    if result["unusual_transactions"].empty:
        report.append("No unusual transactions detected.")
    else:
        for _, row in result["unusual_transactions"].iterrows():
            report.append(
                f"- {row['Department']} | "
                f"{row['Vendor']} | "
                f"${row['Actual']:,.2f}"
            )

    return "\n".join(report)


agent = Agent(
    tools=[analyze_financial_file],
    system_prompt="""
You are FinGuard AI, an autonomous finance analysis agent.

Your purpose is to help finance managers identify important
financial risks without manually checking every transaction.

When asked to analyze financial data:

1. Use the financial analysis tool.
2. Identify budget overruns.
3. Identify unusual transactions.
4. Explain the business impact.
5. Prioritize the most important risks.
6. Give a clear recommendation for the finance manager.

Never make the final financial decision yourself.
The human finance manager remains responsible for approval
and business decisions.

Your responses should be concise, professional, and
executive-friendly.
"""
)


if __name__ == "__main__":
    response = agent(
        "Analyze the company's financial data and tell me "
        "which issues require the finance manager's attention."
    )

    print(response)