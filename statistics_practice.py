import pandas as pd
df = pd.read_csv("transaction_data.csv")

print("Mean:", df["Transaction_Amount"].mean())
print("Mean:", df["Transaction_Amount"].median())
print("Mean:", df["Transaction_Amount"].mode()[0])

print("Variance:", df["Transaction_Amount"].var())
print("Standard Deviation:", df["Transaction_Amount"].std())

correlation = df["Total_Balance"].corr(df["Investment_Amount"])
print("Correlation:", correlation)

print("25th Percentile:", df["Transaction_Amount"].quantile(0.25))
print("50th Percentile (Median):", df["Transaction_Amount"].quantile(0.50))
print("75th Percentile:", df["Transaction_Amount"].quantile(0.75))