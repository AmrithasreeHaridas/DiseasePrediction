import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load Dataset
df = pd.read_csv('predictor/dataset/disease_data.csv')
print(df.columns)
# Split Data
X = df.drop(columns=['Disease'])  # Symptoms as features
y = df['Disease']  # Target variable (Disease)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save Model
with open('predictor/disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")

