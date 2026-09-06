import pandas as pd


def analyze_finances(file_path):
    """Analyze financial data from an Excel file."""

    # Load Excel data
    df = pd.read_excel(file_path)

    # Required columns
    required_columns = ["Department", "Vendor", "Budget", "Actual"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

    # Clean numeric columns
    df["Budget"] = pd.to_numeric(df["Budget"], errors="coerce").fillna(0)
    df["Actual"] = pd.to_numeric(df["Actual"], errors="coerce").fillna(0)

    # Budget variance
    df["Variance"] = df["Actual"] - df["Budget"]

    # Avoid division by zero
    df["Variance_%"] = 0.0

    valid_budget = df["Budget"] != 0

    df.loc[valid_budget, "Variance_%"] = (
        df.loc[valid_budget, "Variance"]
        / df.loc[valid_budget, "Budget"]
    ) * 100

    # Budget overruns
    overruns = df[df["Actual"] > df["Budget"]].copy()

    # Unusual transactions
    average_expense = df["Actual"].mean()

    unusual = df[
        df["Actual"] > average_expense * 2
    ].copy()

    # Overall summary
    total_budget = df["Budget"].sum()
    total_actual = df["Actual"].sum()
    total_variance = total_actual - total_budget

    if total_budget > 0:
        variance_percent = (
            total_variance / total_budget
        ) * 100
    else:
        variance_percent = 0

    # Department-wise analysis
    department_summary = (
        df.groupby("Department")
        .agg(
            Budget=("Budget", "sum"),
            Actual=("Actual", "sum"),
            Transactions=("Actual", "count")
        )
        .reset_index()
    )

    department_summary["Variance"] = (
        department_summary["Actual"]
        - department_summary["Budget"]
    )

    department_summary["Variance_%"] = 0.0

    valid_department_budget = (
        department_summary["Budget"] != 0
    )

    department_summary.loc[
        valid_department_budget, "Variance_%"
    ] = (
        department_summary.loc[
            valid_department_budget, "Variance"
        ]
        / department_summary.loc[
            valid_department_budget, "Budget"
        ]
    ) * 100

    return {
        "data": df,
        "total_budget": total_budget,
        "total_actual": total_actual,
        "total_variance": total_variance,
        "variance_percent": variance_percent,
        "budget_overruns": overruns,
        "unusual_transactions": unusual,
        "department_summary": department_summary,
    }


def create_report(file_path):
    """Create a professional FinGuard AI financial report."""

    result = analyze_finances(file_path)

    print("\n" + "=" * 60)
    print("              FINGUARD AI")
    print("          FINANCIAL ANALYSIS REPORT")
    print("=" * 60)

    print("\n--- OVERALL FINANCIAL SUMMARY ---")

    print(
        f"Total Budget       : "
        f"${result['total_budget']:,.2f}"
    )

    print(
        f"Actual Spending    : "
        f"${result['total_actual']:,.2f}"
    )

    print(
        f"Total Variance     : "
        f"${result['total_variance']:,.2f}"
    )

    print(
        f"Variance %         : "
        f"{result['variance_percent']:.2f}%"
    )

    # Spending status
    print("\n--- FINANCIAL STATUS ---")

    if result["variance_percent"] > 10:
        print(
            "⚠️ HIGH SPENDING ALERT"
        )
        print(
            "Finance manager review is recommended."
        )

    elif result["variance_percent"] > 0:
        print(
            "⚠️ OVER BUDGET"
        )
        print(
            "Actual spending is above the approved budget."
        )

    else:
        print(
            "✅ WITHIN BUDGET"
        )
        print(
            "Overall spending is within the approved budget."
        )

    # Budget overruns
    print("\n--- BUDGET OVERRUNS ---")

    if result["budget_overruns"].empty:
        print("No budget overruns detected.")

    else:
        for _, row in result["budget_overruns"].iterrows():

            print(
                f"{row['Department']} | "
                f"Budget: ${row['Budget']:,.2f} | "
                f"Actual: ${row['Actual']:,.2f} | "
                f"Over: ${row['Variance']:,.2f}"
            )

    # Unusual transactions
    print("\n--- UNUSUAL TRANSACTIONS ---")

    if result["unusual_transactions"].empty:
        print("No unusual transactions detected.")

    else:
        for _, row in result["unusual_transactions"].iterrows():

            print(
                f"{row['Department']} | "
                f"{row['Vendor']} | "
                f"${row['Actual']:,.2f}"
            )

    # Department analysis
    print("\n--- DEPARTMENT ANALYSIS ---")

    department_summary = result["department_summary"]

    for _, row in department_summary.iterrows():

        status = (
            "OVER BUDGET"
            if row["Variance"] > 0
            else "WITHIN BUDGET"
        )

        print(
            f"{row['Department']} | "
            f"Budget: ${row['Budget']:,.2f} | "
            f"Actual: ${row['Actual']:,.2f} | "
            f"Variance: ${row['Variance']:,.2f} | "
            f"{status}"
        )

    # Recommendations
    print("\n--- RECOMMENDATION ---")

    if result["variance_percent"] > 10:

        print(
            "⚠️ Immediate finance manager review recommended."
        )
        print(
            "Spending is significantly above the approved budget."
        )

    elif result["variance_percent"] > 0:

        print(
            "⚠️ Review departments with budget overruns "
            "and control unnecessary spending."
        )

    else:

        print(
            "✅ Spending is currently within the approved budget."
        )

    if not result["unusual_transactions"].empty:

        print(
            "⚠️ Unusual transactions were detected "
            "and should be reviewed."
        )

    print("\n" + "=" * 60)
    print("          FinGuard AI Analysis Complete")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    create_report("data/financial_data.xlsx")