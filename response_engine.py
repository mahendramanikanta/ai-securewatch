"""
Security Response Engine
Applies security controls based on risk severity
"""

def apply_security_response(risk_result, signals):
    actions = []

    severity = risk_result["severity"]

    if severity == "Low":
        actions.append("Activity logged for monitoring")

    elif severity == "Medium":
        actions.append("SOC alert generated")
        actions.append("User activity flagged for review")

    elif severity == "High":
        actions.append("Multi-factor authentication enforced")
        actions.append("SOC team notified")
        actions.append("Session marked as high-risk")

    elif severity == "Critical":
        actions.append("User account temporarily locked")
        actions.append("Source IP address blocked")
        actions.append("SOC team notified immediately")
        actions.append("Incident escalated to security admin")

    return actions
