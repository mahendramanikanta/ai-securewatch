import pandas as pd
from sklearn.ensemble import IsolationForest

# Load and train once
data = pd.read_csv("ai/security_logs.csv")
X = data[["hour", "failed_logins", "requests_per_min", "role_access"]]

model = IsolationForest(contamination=0.25, random_state=42)
model.fit(X)

def detect_anomaly(input_data):
    """
    input_data: dict with keys
    hour, failed_logins, requests_per_min, role_access
    """
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    if prediction == -1:
        return "Anomaly"
    return "Normal"
