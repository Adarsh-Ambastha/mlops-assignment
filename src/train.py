import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("data/data.csv")
df = pd.read_csv("data/data.csv", header=None, names=['x', 'y'])
X = df[['x']]
y = df['y']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'model.pkl')