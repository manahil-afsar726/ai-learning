import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("transaction_data.csv")
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Year"] = df["Transaction_Date"].dt.year
yearly_total = df.groupby("Year")["Transaction_Amount"].sum()

yearly_total.plot(kind="bar")
plt.title("Total Transaction Amount by Year")
plt.xlabel("Year")
plt.ylabel("Total Transaction Amount")
plt.show()

yearly_total.plot(kind="line", marker="o")
plt.title("Total Transaction Amount by Year")
plt.xlabel("Year")
plt.ylabel("Total Transaction Amount")
plt.show()

account_counts = df["Account_Type"].value_counts()
account_counts.plot(kind="pie", autopct= "%1.1f%%")
plt.title("Account Type Distribution")
plt.ylabel("")
plt.show()

df["Transaction_Amount"].plot(kind="hist", bins=20)
plt.title("Distribution of Transaction Amount")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df["Total_Balance"], df["Investment_Amount"], alpha=0.1)
plt.title("Total Balance vs Investment Amount")
plt.xlabel("Total Balance")
plt.ylabel("Investment Amount")
plt.show()
