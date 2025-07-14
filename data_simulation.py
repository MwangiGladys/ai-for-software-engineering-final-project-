import pandas as pd
import numpy as np
import os

# Simulate 1 week's worth of minute-by-minute health data
data = {
    'timestamp': pd.date_range(start='2025-07-01', periods=10080, freq='T'),  # 7 days, 1-minute intervals
    'heart_rate': np.random.randint(60, 100, 10080),
    'blood_oxygen': np.random.randint(90, 100, 10080),
    'activity_level': np.random.choice(['low', 'moderate', 'high'], 10080)
}

df = pd.DataFrame(data)

# Save to CSV in the data folder
os.makedirs('../data', exist_ok=True)
df.to_csv('data/simulated_health_data.csv', index=False)
print("✅ Simulated health data saved to /data/simulated_health_data.csv")
