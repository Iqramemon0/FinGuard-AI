import pandas as pd

data = [
    ["Marketing", "Advertising", "Google Ads", 50000, 68000],
    ["IT", "Software", "Microsoft", 80000, 76000],
    ["HR", "Recruitment", "LinkedIn", 30000, 42000],
    ["Operations", "Supplies", "Office Depot", 45000, 47000],
    ["Sales", "Travel", "Emirates", 35000, 31000],
    ["Marketing", "Events", "Expo Events", 25000, 39000],
    ["IT", "Hardware", "Dell", 40000, 92000],
    ["HR", "Training", "Training Vendor", 20000, 18000],
    ["Operations", "Maintenance", "ABC Services", 30000, 28000],
    ["Sales", "Advertising", "Facebook Ads", 22000, 27000],
]

df = pd.DataFrame(
    data,
    columns=["Department", "Category", "Vendor", "Budget", "Actual"]
)

df.to_excel("data/financial_data.xlsx", index=False)

print("✅ Financial dataset created successfully!")
print("📁 File: data/financial_data.xlsx")
