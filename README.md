# 🛡️ AI SecureWatch

### AI-Driven Cloud Security Monitoring Platform (SOC Simulation)

> **AI SecureWatch** is an AI-assisted cloud security monitoring platform inspired by **Microsoft Azure Sentinel**.
> It detects anomalous user behavior, evaluates security risk, classifies severity, logs incidents, and simulates automated SOC (Security Operations Center) responses in real time.

---

## 📌 Table of Contents

* [Problem Statement](#-problem-statement)
* [Why AI SecureWatch?](#-why-ai-securewatch)
* [Key Features](#-key-features)
* [System Architecture](#-system-architecture)
* [AI & Security Logic](#-ai--security-logic)
* [Project Structure](#-project-structure)
* [How It Works (Flow)](#-how-it-works-flow)
* [Installation & Local Setup](#-installation--local-setup)
* [Running the Application](#-running-the-application)
* [Cloud Deployment](#-cloud-deployment)
* [Security Design](#-security-design)
* [Screenshots](#-screenshots)
* [Future Enhancements](#-future-enhancements)
* [License](#-license)
* [Author](#-author)

---

## ❓ Problem Statement

Modern cloud applications face increasing security threats such as:

* Credential abuse
* Account takeover attacks
* Privilege misuse
* Brute-force login attempts
* Abnormal traffic spikes

Traditional security systems react **after damage occurs**.

**Problem:**

> How can we detect suspicious behavior early, assess risk intelligently, and respond automatically?

---

## 💡 Why AI SecureWatch?

AI SecureWatch addresses this by:

* Continuously analyzing user behavior patterns
* Detecting anomalies using AI-assisted logic
* Assigning **risk scores and severity levels**
* Triggering **automated security actions**
* Providing a **SOC-style monitoring dashboard**

It simulates how **enterprise security platforms (Azure Sentinel / SIEM systems)** operate — in a lightweight, educational, and extendable form.

---

## ✨ Key Features

### 🔍 Threat Detection

* Failed login spike detection
* Abnormal request rate detection
* Suspicious admin access detection
* IP reputation analysis

### 📊 Risk & Severity Assessment

* Risk score (0–100%)
* Severity levels: `Low`, `Medium`, `High`, `Critical`

### 🤖 Automated Security Actions

* Temporary account lock
* IP address blocking
* SOC team notification
* Incident escalation

### 📜 Security Logging

* Timestamped incident logs
* Severity-based log classification
* Real-time incident feed in UI

### 🖥️ SOC Dashboard UI

* Real-time analysis
* Visual risk indicators
* Color-coded alerts
* Incident history viewer

---

## 🏗️ System Architecture

```
User Input
   ↓
Signal Engine (Behavior Signals)
   ↓
Risk Engine (Risk Score Calculation)
   ↓
Response Engine (Security Actions)
   ↓
Security Logger (Incident Logging)
   ↓
SOC Dashboard (UI)
```

---

## 🧠 AI & Security Logic

AI SecureWatch uses **AI-assisted rule intelligence** (ML-ready architecture):

### Behavioral Signals

* Login hour anomaly
* Failed login frequency
* Requests per minute
* Role access level
* IP reputation

### Risk Calculation

Each signal contributes weighted risk points.
Final risk score is computed and mapped to severity:

| Risk Score | Severity |
| ---------- | -------- |
| 0–30       | Low      |
| 31–60      | Medium   |
| 61–80      | High     |
| 81–100     | Critical |

---

## 📂 Project Structure

```
ai-securewatch/
│
├── ai/
│   ├── signal_engine.py
│   ├── risk_engine.py
│   ├── response_engine.py
│   ├── anomaly_detection.py
│
├── static/
│   ├── soc.js
│   ├── soc.css
│
├── templates/
│   └── index.html
│
├── app_ai.py
├── security_logger.py
├── security.log
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🔄 How It Works (Flow)

1. User submits behavior data from UI
2. API validates request via API key
3. Signal Engine extracts suspicious indicators
4. Risk Engine calculates risk score & severity
5. Response Engine determines security actions
6. Incident is logged securely
7. Dashboard updates in real time

---

## ⚙️ Installation & Local Setup

### Prerequisites

* Python 3.9+
* Git

### Clone Repository

```bash
git clone https://github.com/mahendramanikanta/ai-securewatch.git
cd ai-securewatch
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app_ai.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## ☁️ Cloud Deployment

AI SecureWatch is cloud-deployed and publicly accessible.

### Supported Platforms

* Render (Free tier)
* Railway
* Azure App Service (recommended for enterprise scaling)

Deployment uses:

* GitHub CI integration
* Python web service
* Environment-based API key security

---

## 🔐 Security Design

* API key authentication
* Input validation
* Incident logging isolation
* Severity-based alerting
* No sensitive credentials committed to repo

---

## 🚀 Future Enhancements

* Machine Learning model integration (Isolation Forest / Autoencoders)
* Real cloud log ingestion (Azure Monitor / AWS CloudWatch)
* Role-based UI access
* Email / Slack alerts
* Dashboard analytics charts
* Azure Sentinel connector integration

---

## 📜 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.

---

## 👨‍💻 Author

**Manikanta**

* Cloud & AI Security Enthusiast
* AI SecureWatch – 2026
* © All rights reserved

---