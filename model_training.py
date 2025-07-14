import pandas as pd
from sklearn.ensemble import IsolationForest
import os

# Load the simulated health data
df = pd.read_csv('data/simulated_health_data.csv')

# Prepare the numeric columns for modeling
X = df[['heart_rate', 'blood_oxygen']]

# Initialize the Isolation Forest model
model = IsolationForest(contamination=0.01, random_state=42)
df['anomaly'] = model.fit_predict(X)

# Convert anomaly labels to readable text
df['anomaly'] = df['anomaly'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')

# Save the results into a new CSV
df.to_csv('data/health_data_with_anomalies.csv', index=False)

print("✅ Anomaly detection complete. Results saved to /data/health_data_with_anomalies.csv")
