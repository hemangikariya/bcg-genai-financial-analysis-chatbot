import pandas as pd

try:
    df = pd.read_csv("financial_data.csv")
except FileNotFoundError:
    print("financial_data.csv not found.")
    raise SystemExit

print("="*50)
print("GFC Financial AI Chatbot")
print("="*50)
print("Type 'help' for supported queries or 'exit' to quit.\n")

def summary(company):
    row=df[(df["Company"]==company)&(df["Year"]==2025)].iloc[0]
    return f"""
{company} Financial Summary (2025)
Revenue: {row['Total Revenue']} million USD
Net Income: {row['Net Income']} million USD
Total Assets: {row['Total Assets']} million USD
Total Liabilities: {row['Total Liabilities']} million USD
Operating Cash Flow: {row['Operating Cash Flow']} million USD
"""

while True:
    q=input("You: ").lower().strip()

    if q=="exit":
        print("Bot: Thank you!")
        break

    elif q=="help":
        print("""
Supported Queries:
- What is Microsoft's revenue in 2025?
- What is Apple's net income in 2025?
- Show Tesla operating cash flow in 2025.
- Compare Microsoft and Apple revenue.
- Which company has the highest revenue?
- Which company has the highest net income?
- Microsoft summary
- Apple summary
- Tesla summary
""")

    elif "microsoft" in q and "revenue" in q:
        v=df[(df.Company=="Microsoft")&(df.Year==2025)]["Total Revenue"].iloc[0]
        print(f"Bot: Microsoft's Revenue in 2025 is {v} million USD.")

    elif "apple" in q and "net income" in q:
        v=df[(df.Company=="Apple")&(df.Year==2025)]["Net Income"].iloc[0]
        print(f"Bot: Apple's Net Income in 2025 is {v} million USD.")

    elif "tesla" in q and "cash flow" in q:
        v=df[(df.Company=="Tesla")&(df.Year==2025)]["Operating Cash Flow"].iloc[0]
        print(f"Bot: Tesla Operating Cash Flow in 2025 is {v} million USD.")

    elif "compare" in q and "revenue" in q:
        for c in ["Microsoft","Apple"]:
            r=df[(df.Company==c)&(df.Year==2025)]["Total Revenue"].iloc[0]
            print(f"{c}: {r} million USD")

    elif "highest revenue" in q:
        row=df[df.Year==2025].sort_values("Total Revenue",ascending=False).iloc[0]
        print(f"Bot: {row['Company']} has the highest revenue ({row['Total Revenue']} million USD).")

    elif "highest net income" in q:
        row=df[df.Year==2025].sort_values("Net Income",ascending=False).iloc[0]
        print(f"Bot: {row['Company']} has the highest net income ({row['Net Income']} million USD).")

    elif "microsoft summary" in q:
        print(summary("Microsoft"))
    elif "apple summary" in q:
        print(summary("Apple"))
    elif "tesla summary" in q:
        print(summary("Tesla"))
    else:
        print("Bot: Sorry, I support only predefined financial queries.")
