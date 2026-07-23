import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("transaction_data.csv")
X = df[["Total_Balance"]]
y = df["Investment_Amount"]

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained successfully!")

predictions=model.predict(X_test)
print("Actual values:", y_test.values[:5])
print("Prediction values:", predictions[:5])

from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(y_test,predictions)
r2 = r2_score(y_test, predictions)
print("mean square error:", mse)
print("R2 score:", r2)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X2 = df[["Total_Balance"]]
y2 = df[["Account_Type"]]

X2_train, X2_test, y2_train, y2_test = train_test_split(X2,y2, test_size=0.2, random_state=42)

clf_model = LogisticRegression()
clf_model.fit(X2_train, y2_train)

predictions2 = clf_model.predict(X2_test)

accuracy = accuracy_score(y2_test, predictions2)
print("Classification Accuracy:", accuracy)