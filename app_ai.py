import os
from flask import Flask, request, jsonify, render_template

from signal_engine import extract_signals
from risk_engine import calculate_risk
from response_engine import apply_security_response
from security_logger import log_security_event

app = Flask(__name__)

# 🔐 API Key (from environment for security)
API_KEY = os.getenv("API_KEY")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_security():
    # --- API key validation ---
    client_key = request.headers.get("X-API-KEY")
    if client_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    # --- Validate JSON ---
    activity = request.get_json()
    if not activity:
        return jsonify({"error": "Invalid input"}), 400

    try:
        # 1️⃣ Signal extraction
        signals = extract_signals(activity)

        # 2️⃣ Risk calculation
        risk = calculate_risk(signals)

        # 3️⃣ Automated security response
        actions = apply_security_response(risk, signals)

        # 4️⃣ Log serious incidents
        if risk["severity"] in ["High", "Critical"]:
            log_security_event(
                f"[SECURITY INCIDENT] "
                f"Severity={risk['severity']} | "
                f"Risk={risk['risk_score']} | "
                f"Threat={risk['threat_type']} | "
                f"Actions={actions}"
            )

        return jsonify({
            "risk_score": risk["risk_score"],
            "severity": risk["severity"],
            "threat_type": risk["threat_type"],
            "reasons": risk["reasons"],
            "actions": actions
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/incidents", methods=["GET"])
def incidents():
    try:
        with open("security.log", "r") as f:
            logs = f.readlines()[-15:]
    except FileNotFoundError:
        logs = []

    return jsonify({"incidents": logs})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
