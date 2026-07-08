import pandas as pd
data = {
    "name" : ["ali", "sara", "ahmed", "zara"],
    "departement" : ["IT", "HR", "FINANCE", "IT"],
    "salary" : [50000, 45000, 55000, 52000],
    "Experience": [3,2,5,4]
}
df = pd.DataFrame(data)
print(df)
print("\naverage salary:", df["salary"].mean())
print("maximum salary:", df["salary"].max())

print("\nIT DEPARTMENT EMPLOYEES")
print(df[df["departement"]=="IT"])

print("\nHIGHEST SALARY EMPLOYEE:")
print(df[df["salary"]== df["salary"].max()])

print("\nASCENDING ORDER:")
print(df.sort_values("salary"))

print("\nDESCENDING ORDER:")
print(df.sort_values("salary", ascending=False))

