# air-gapped-noc-copilot
# 🛡️ Air-Gapped Predictive Copilot for Secure MPLS Operations

### **Team Name:** Binary Codes  
### **Event:** ISRO Bharatiya Antariksh Hackathon 2026 (BAH 2026)  

---

## 📋 Project Overview
Modern critical networks operating under strict **air-gap constraints** cannot rely on cloud-connected AI infrastructure. **Binary Codes** introduces an autonomous, completely offline network operational resilience platform that predicts failures, detects threat patterns, ensures compliance, and offers localized LLM guidance for complex SD-WAN over MPLS topologies.

This system integrates three conceptual frameworks into one single unified engineering stream:
1. **Aegis-Net (SecOps Module):** Real-time monitoring for behavioral anomalies, dynamic BGP hijacking detection, and security profile drifts.
2. **Pulse-Check (Health Module):** Heavy telemetry processing calculating jitter stability gradients and early warning parameters before service breach.
3. **Sentinel-SandBox (Disaster Recovery Module):** Automated compliance checks, configuration protection, and local localized configuration rollback states.

---

## 📁 System Architecture & Directory Layout

```text
air-gapped-noc-copilot/
│
├── simulator/
│   └── network_sim.py       # Ingests multi-site telemetry & dynamic failure scenarios
│
├── aegis_secops/            # [Idea 1] Focus: Cyber-Security Engine
│   └── threat_detector.py   
│
├── pulse_health/            # [Idea 2] Focus: Network Health Monitoring Engine
│   └── maintenance_ml.py    
│
├── sentinel_recovery/       # [Idea 3] Focus: Disaster Recovery & Compliance Configuration
│   └── backup_compliance.py 
│
├── copilot_rag/             # [AI Brain] Air-gapped Retrieval Context & Local LLM Connector
│   └── llm_handler.py       
│
├── app.py                   # Central Unified Streamlit Executive Dashboard
└── requirements.txt         # Project Baseline Dependencies
