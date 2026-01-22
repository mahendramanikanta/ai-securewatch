document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("analyzeBtn").addEventListener("click", analyze);
  loadIncidents();
});

async function analyze() {
  const payload = {
    hour: +hour.value,
    failed_logins: +failed.value,
    requests_per_min: +rpm.value,
    role_access: +role.value,
    ip_reputation: +iprep.value
  };

  if (Object.values(payload).some(v => isNaN(v))) {
    alert("Please fill all fields correctly");
    return;
  }

  setStatus("Analyzing…", "warning");

  const res = await fetch("/analyze", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-API-KEY": "manikanta-securewatch-key"
    },
    body: JSON.stringify(payload)
  });

  const data = await res.json();
  updateUI(data);
  loadIncidents();
}

function updateUI(data) {
  riskScore.innerText = data.risk_score + "%";
  severity.innerText = data.severity;

  if (data.severity === "Critical" || data.severity === "High") {
    setStatus("🚨 SECURITY ALERT", "danger");
  } else {
    setStatus("✔ SYSTEM READY", "success");
  }

  actions.innerHTML = "";
  data.actions.forEach(a => {
    const p = document.createElement("p");
    p.innerText = "✔ " + a;
    p.className = "text-emerald-400";
    actions.appendChild(p);
  });
}

function setStatus(text, type) {
  statusBox.className =
    "bg-slate-800/70 rounded-xl p-5 flex items-center justify-between border";

  if (type === "danger") statusBox.classList.add("border-red-500");
  else if (type === "warning") statusBox.classList.add("border-yellow-400");
  else statusBox.classList.add("border-emerald-400");

  statusBox.querySelector("p.text-xl").innerText = text;
}

async function loadIncidents() {
  const res = await fetch("/incidents");
  const data = await res.json();

  incidentList.innerHTML = "";
  data.incidents.forEach(line => {
    const li = document.createElement("li");

    if (line.includes("CRITICAL")) li.className = "text-red-400";
    else if (line.includes("WARNING")) li.className = "text-yellow-400";
    else li.className = "text-slate-400";

    li.textContent = line;
    incidentList.appendChild(li);
  });
}
