from flask import Flask, request, jsonify, render_template
from signal_engine import extract_signals
from risk_engine import calculate_risk
from response_engine import apply_security_response
from security_logger import log_security_event

app = Flask(__name__)

# 🔐 Simple API protection
API_KEY = "manikanta-securewatch-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_security():
    # --- API key check ---
    client_key = request.headers.get("X-API-KEY")
    if client_key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    activity = request.json

    # 1️⃣ Signal extraction
    signals = extract_signals(activity)

    # 2️⃣ Risk calculation
    risk = calculate_risk(signals)

    # 3️⃣ Security response
    actions = apply_security_response(risk, signals)

    # 4️⃣ Logging critical incidents
    if risk["severity"] in ["High", "Critical"]:
        log_security_event(
            f"[INCIDENT] Severity={risk['severity']} | "
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


@app.route("/incidents", methods=["GET"])
def incidents():
    try:
        with open("security.log", "r") as f:
            logs = f.readlines()[-15:]
    except FileNotFoundError:
        logs = []

    return jsonify({"incidents": logs})


if __name__ == "__main__":
    app.run(debug=False)
