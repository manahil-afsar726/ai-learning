import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("transaction_data.csv")

sns.histplot(df["Transaction_Amount"], bins=20, kde=True)
plt.title("Transaction Amount Distribution(Seaborn)")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.show()

sns.boxplot(x="Account_Type", y="Total_Balance", data=df)
plt.title("Total Balance by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Total Balance")
plt.show()

numeric_df = df[["Total_Balance", "Transaction_Amount", "Investment_Amount"]]
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Barplot - average balance by account type
sns.barplot(x="Account_Type", y="Total_Balance", data=df)
plt.title("Average Total Balance by Account Type")
plt.xlabel("Account Type")
plt.ylabel("Average Total Balance")
plt.show()

# Countplot - kitni baar har account type aaya
sns.countplot(x="Account_Type", data=df)
plt.title("Count of Each Account Type")
plt.xlabel("Account Type")
plt.ylabel("Count")
plt.show()

# Scatterplot - do numbers ka rishta
sns.scatterplot(x="Total_Balance", y="Investment_Amount", data=df, alpha=0.3)
plt.title("Total Balance vs Investment Amount")
plt.xlabel("Total Balance")
plt.ylabel("Investment Amount")
plt.show()

# Violin plot - boxplot + distribution shape
sns.violinplot(x="Account_Type", y="Total_Balance", data=df)
plt.title("Balance Distribution by Account Type (Violin)")
plt.xlabel("Account Type")
plt.ylabel("Total Balance")
plt.show()

# Pairplot - sab numeric columns ka ek sath comparison
numeric_df = df[["Total_Balance", "Transaction_Amount", "Investment_Amount"]]
sns.pairplot(numeric_df)
plt.show()