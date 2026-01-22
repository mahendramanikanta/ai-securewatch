"""
Risk Engine
Calculates risk score, severity, and threat type
based on security signals.
"""

def calculate_risk(signals):
    risk_score = 0
    reasons = []

    # 1. Failed login attempts
    if signals["failed_logins"] >= 5:
        risk_score += 25
        reasons.append("Multiple failed login attempts")

    # 2. High request rate (possible bot / abuse)
    if signals["requests_per_min"] >= 100:
        risk_score += 25
        reasons.append("Abnormally high request rate")

    # 3. Admin role misuse
    if signals["role_access"] == 2 and signals["requests_per_min"] >= 80:
        risk_score += 20
        reasons.append("Suspicious admin activity")

    # 4. Suspicious IP reputation
    if signals["ip_reputation"] == 1:
        risk_score += 20
        reasons.append("Known suspicious IP source")

    # 5. Unusual login time
    if signals["login_hour"] <= 5:
        risk_score += 10
        reasons.append("Unusual login time")

    # Cap score at 100
    risk_score = min(risk_score, 100)

    # Severity classification
    if risk_score >= 80:
        severity = "Critical"
        threat_type = "Credential Abuse / Account Takeover"
    elif risk_score >= 60:
        severity = "High"
        threat_type = "Privilege Misuse"
    elif risk_score >= 40:
        severity = "Medium"
        threat_type = "Suspicious Behavior"
    else:
        severity = "Low"
        threat_type = "Normal Activity"

    return {
        "risk_score": risk_score,
        "severity": severity,
        "threat_type": threat_type,
        "reasons": reasons
    }
