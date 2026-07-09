import pandas as pd
df = pd.read_csv("transaction_data.csv")
print(df.head())

print("\nData Info")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nColumn names:")
for col in df.columns:
    print(col)

print("\nColumn names:")
print(df.columns.tolist())

print("\nAverage Total Balance:")
print(df["Total_Balance"].mean())

print("\nInvestment by Type:")
print(df.groupby("Investment_Type")["Investment_Amount"].sum())

print("\nCustomers by Account Type:")
print(df["Account_Type"].value_counts())

business_df = df[df["Account_Type"]=="Business"]
print(business_df.head())
print("\nTotal Business Rows:")
print(len(business_df))

print("\nDESCENDING ORDER:")
sorted_df=df.sort_values("Total_Balance", ascending=False)
print(sorted_df[["Account_Type", "Total_Balance"]].head(10))

print("\nTransaction Date:")
print(df["Transaction_Date"].dtype)
df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
df["Year"] = df["Transaction_Date"].dt.year
print(df["Year"].head())
yearly_total=df.groupby("Year")["Transaction_Amount"].sum()
print(yearly_total)

result = df.groupby(["Account_Type", "Investment_Type"]) ["Investment_Amount"].mean()
print(result)

print(df.isnull().sum())

pivot=df.pivot_table(index="Account_Type", columns="Investment_Type", values="Transaction_Amount",aggfunc="mean")
print(pivot)

result = df[(df["Account_Type"]=="Savings") & (df["Total_Balance"]>50000)]
print(len(result))

print(df["Investment_Type"].value_counts())

print("Max Transaction:", df["Transaction_Amount"].max())
print("Min Transaction:", df["Transaction_Amount"].min())

df["Investment_Percentage"] = (df["Investment_Amount"] / df["Total_Balance"])*100
print(df[["Total_Balance", "Investment_Amount", "Investment_Percentage"]].head())
