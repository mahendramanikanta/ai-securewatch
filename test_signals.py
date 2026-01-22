from signal_engine import extract_signals

sample_activity = {
    "login_hour": 2,
    "failed_logins": 6,
    "requests_per_min": 140,
    "role_access": 2,
    "ip_reputation": 1
}

signals = extract_signals(sample_activity)
print(signals)
