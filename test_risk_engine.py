from risk_engine import calculate_risk

signals = {
    "login_hour": 2,
    "failed_logins": 7,
    "requests_per_min": 140,
    "role_access": 2,
    "ip_reputation": 1
}

result = calculate_risk(signals)
print(result)
