"""
Signal Engine
Extracts meaningful security signals from user activity
"""

def extract_signals(activity):
    """
    activity: dict containing raw access data
    returns: validated security signals
    """

    signals = {
        "login_hour": int(activity.get("login_hour", 0)),
        "failed_logins": int(activity.get("failed_logins", 0)),
        "requests_per_min": int(activity.get("requests_per_min", 0)),
        "role_access": int(activity.get("role_access", 1)),  # 1=user, 2=admin
        "ip_reputation": int(activity.get("ip_reputation", 0))  # 0=clean, 1=suspicious
    }

    return signals
