import pandas as pd
from sklearn.ensemble import IsolationForest

# Load security log data
data = pd.read_csv("security_logs.csv")

# Features used for ML
X = data[["hour", "failed_logins", "requests_per_min", "role_access"]]

# Train Isolation Forest (unsupervised ML)
model = IsolationForest(contamination=0.25, random_state=42)
model.fit(X)

# Predict anomalies
data["prediction"] = model.predict(X)
data["prediction"] = data["prediction"].map({1: "Normal", -1: "Anomaly"})

print("\n=== AI-Based Cloud Threat Detection Results ===")
print(data)
