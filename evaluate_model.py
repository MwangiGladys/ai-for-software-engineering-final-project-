import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Load the health data with anomalies
df = pd.read_csv('data/health_data_with_anomalies.csv')

# Prepare the features and target
X = df[['heart_rate', 'blood_oxygen']]
y = df['anomaly'].apply(lambda x: 1 if x == 'Anomaly' else 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple classifier for evaluation (Random Forest)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Generate and display the classification report
report = classification_report(y_test, y_pred)
print("\n🔍 EVALUATION RESULTS:\n")
print(report)
