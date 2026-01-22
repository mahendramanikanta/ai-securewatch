from response_engine import apply_security_response

risk_result = {
    "risk_score": 90,
    "severity": "Critical",
    "threat_type": "Credential Abuse"
}

signals = {
    "login_hour": 2,
    "failed_logins": 7,
    "requests_per_min": 140,
    "role_access": 2,
    "ip_reputation": 1
}

actions = apply_security_response(risk_result, signals)
print(actions)
