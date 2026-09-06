# 🛡️ FinGuard AI

**FinGuard AI** is an intelligent financial analysis agent designed to automate repetitive finance tasks, monitor budgets, detect unusual transactions, and generate actionable financial insights from Excel data.

The project is designed to help finance teams quickly identify budget overruns, spending risks, and departments that require management attention.

---

## 🚀 Project Goal

FinGuard AI transforms raw financial data into meaningful financial insights.

It analyzes financial transactions and automatically:

* 📊 Calculates total budget and actual spending
* 💰 Calculates budget variance
* 📈 Calculates variance percentage
* 🚨 Detects budget overruns
* 🔎 Identifies unusual high-value transactions
* 🏢 Performs department-wise financial analysis
* 💡 Generates automated finance recommendations

---

## ✨ Key Features

### 1. Budget Variance Analysis

FinGuard AI compares approved budgets with actual spending and calculates:

* Total Budget
* Actual Spending
* Total Variance
* Variance Percentage

### 2. Budget Overrun Detection

The system automatically identifies departments or transactions where:

**Actual Spending > Budget**

This helps finance managers quickly identify areas of overspending.

### 3. Unusual Transaction Detection

Transactions significantly higher than the average spending level are automatically flagged for review.

### 4. Department-Level Analysis

FinGuard AI summarizes financial performance by department, including:

* Department Budget
* Department Actual Spending
* Variance
* Variance Percentage
* Number of Transactions
* Budget Status

### 5. Automated Recommendations

The system generates recommendations based on financial performance.

For example:

> ⚠️ Immediate finance manager review recommended.

when spending is significantly above the approved budget.

---

## 🛠️ Technologies

* **Python**
* **Pandas**
* **Excel**
* **CSV**
* **Strands Agents SDK**
* **AWS**
* **Power BI**

---

## 📁 Project Structure

```text
FinGuard-AI/
│
├── data/
│   └── financial_data.xlsx
│
├── finance_analysis.py
│
├── README.md
│
└── requirements.txt
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Iqramemon0/FinGuard-AI.git
cd FinGuard-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / GitHub Codespaces:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install pandas openpyxl
```

### 5. Run FinGuard AI

```bash
python finance_analysis.py
```

The system will analyze:

```text
data/financial_data.xlsx
```

and generate a financial analysis report in the terminal.

---

## 📊 Sample Output

```text
========== FINGUARD AI FINANCIAL REPORT ==========

--- OVERALL FINANCIAL SUMMARY ---

Total Budget
Actual Spending
Total Variance
Variance %

--- FINANCIAL STATUS ---

⚠️ HIGH SPENDING ALERT

--- BUDGET OVERRUNS ---

Department | Budget | Actual | Over

--- UNUSUAL TRANSACTIONS ---

Department | Vendor | Amount

--- DEPARTMENT ANALYSIS ---

Department | Budget | Actual | Variance | Status

--- RECOMMENDATION ---

⚠️ Immediate finance manager review recommended.
Spending is significantly above the approved budget.

============================================================
          FinGuard AI Analysis Complete
============================================================
```

---

## 🎯 Hackathon Track

**Professional Agents**

FinGuard AI focuses on applying intelligent automation to real-world financial analysis and decision-making.

---

## 💼 Business Value

FinGuard AI can help finance teams:

* Reduce manual financial analysis
* Identify overspending faster
* Improve budget monitoring
* Detect potentially unusual transactions
* Prioritize management review
* Turn raw financial data into actionable insights

---

## 🔮 Future Improvements

Future versions of FinGuard AI can include:

* 🤖 AI-powered financial explanations
* 📧 Automated finance alerts
* 📊 Interactive Power BI dashboards
* ☁️ AWS-based deployment
* 📄 Automated PDF financial reports
* 🔐 Role-based access control
* 📈 Predictive budget forecasting
* 🧠 Advanced anomaly detection
* 💬 Natural-language finance assistant

---

## 🏆 Project Status

**✅ Functional Prototype**

FinGuard AI currently performs automated financial analysis using Excel data and generates budget, variance, anomaly, department-level, and recommendation insights.

---

## 👩‍💻 Author

**Iqra Memon**

Finance & Business Intelligence Professional

Skills: **Power BI • Python • Excel • Financial Analysis • Data Analytics • Business Intelligence**

---

## 📄 License

This project is developed for educational, portfolio, and hackathon purposes.

````

### Step 3 — Save

README ke andar paste karne ke baad:

**Ctrl + S**

Phir Terminal mein:

```bash
git add README.md
git commit -m "Create professional project README"
git push
```