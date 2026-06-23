# FILE PATH: app.py
import streamlit as st
import time
import pandas as pd

# Core sub-modules connection references
from simulator.network_sim import generate_telemetry_stream
from aegis_secops.threat_detector import inspect_security_posture
from pulse_health.maintenance_ml import predict_line_degradation
from sentinel_recovery.backup_compliance import check_compliance_and_dr
from copilot_rag.llm_handler import ask_offline_copilot

# 1. UI Styling & Page Configuration
st.set_page_config(page_title="Binary Codes | Multi-Engine NOC", layout="wide")

# Custom Dark Theme CSS Injection
st.markdown("""
    <style>
        body { background-color: #0e1117; color: #ffffff; }
        .metric-card { background-color: #1f293d; padding: 20px; border-radius: 10px; border: 1px solid #38bdf8; text-align: center; }
        .section-header { color: #38bdf8; font-weight: bold; border-bottom: 2px solid #38bdf8; padding-bottom: 5px; }
    </style>
""", unsafe_style_html=True)

# 2. Main Executive Header
st.title("🛡️ Air-Gapped Predictive Copilot Engine")
st.markdown("### **Team: Binary Codes** | *ISRO Bharatiya Antariksh Hackathon 2026*")
st.caption("Synchronized Security Architecture: Aegis-Net (SecOps) • Pulse-Check (Health) • Sentinel-SandBox (Recovery)")
st.markdown("---")

# 3. Session State History Tracking (For Time-Series Graphing)
if "history" not in st.session_state:
    st.session_state.history = []

# 4. Sidebar Control Tower Configuration
st.sidebar.header("🕹️ Simulation Control Tower")
scenario = st.sidebar.selectbox("Inject Network Fault Vector", ["Normal Operations", "link_congestion", "bgp_flap"])

# Data Parsing Pipeline
actual_fault = None if scenario == "Normal Operations" else scenario
current_data = generate_telemetry_stream(fault_type=actual_fault)
st.session_state.history.append(current_data)

# Restrict queue size to avoid data blowup
if len(st.session_state.history) > 20: 
    st.session_state.history.pop(0)

# Convert history to DataFrame for graphing
df_history = pd.DataFrame(st.session_state.history)

# 5. Visual Dashboard Grid Architecture
col_metrics, col_analytics = st.columns([1, 1])

with col_metrics:
    st.markdown("<h3 class='section-header'>📊 Ingested Network Telemetry</h3>", unsafe_style_html=True)
    st.write("")
    
    # Live Parameter Badges
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.metric(label="Interface CPU Load", value=f"{current_data['cpu_utilization_pct']}%", delta="-2.4%" if scenario=="Normal Operations" else "+45.1%")
    with m_col2:
        st.metric(label="Link Jitter", value=f"{current_data['jitter_ms']} ms", delta="Stable" if scenario=="Normal Operations" else "Volatile")
    with m_col3:
        st.metric(label="Packet Loss Rate", value=f"{current_data['packet_loss_pct']}%")
        
    st.write("")
    
    # Time-Series Real-time Graph Validation
    st.markdown("#### Real-time Interface Metric Timeline")
    if not df_history.empty and 'cpu_utilization_pct' in df_history.columns:
        st.line_chart(df_history.set_index('timestamp')[['cpu_utilization_pct', 'jitter_ms']])
    
    st.markdown("#### Raw Ingested Syslog Stream Object")
    st.json(current_data)

with col_analytics:
    st.markdown("<h3 class='section-header'>🧠 Predictive Copilot Insights</h3>", unsafe_style_html=True)
    st.write("")
    
    # 1. Trigger Pulse-Check (Network Health Engine)
    health_analysis = predict_line_degradation(st.session_state.history)
    st.info(f"📈 **[Pulse-Check Health Matrix]:** State -> {health_analysis['health_trend']} | Estimated Impact window: {health_analysis.get('time_to_failure', 'N/A')}")
    
    # 2. Trigger Aegis-Net (Cybersecurity Threat Engine)
    security_analysis = inspect_security_posture(current_data)
    if security_analysis["threat_detected"] != "None":
        st.error(f"⚔️ **[Aegis-Net Cryptographic Alert]:** Threat Detected: {security_analysis['threat_detected']} | Operational Risk Profile: **{security_analysis['risk_level']}**")
    else:
        st.success("⚔️ **[Aegis-Net Security Status]:** Integrity Validation Passed. Tunnels secure.")
        
    # 3. Trigger Sentinel-SandBox (DR & Local Compliance Automation)
    dr_compliance = check_compliance_and_dr(actual_fault)
    st.warning(f"🔒 **[Sentinel-SandBox Automation Log]:** Enforcement Action -> {dr_compliance['automated_dr_action']}")
    
    # 4. Local Large Language Model Execution Block
    if actual_fault:
        st.markdown("---")
        st.markdown("### 🤖 Orchestrated Remediation Strategy (Offline AI)")
        combined_context = f"Health Parameters: {health_analysis}, Defensive Threats Status: {security_analysis}, Compliance Framework: {dr_compliance}"
        
        with st.spinner("Analyzing operational signals using local model weights..."):
            ai_response = ask_offline_copilot(scenario, combined_context)
            st.markdown(ai_response)

# Continuous integration framework loop timeline refresh (4 Seconds)
time.sleep(4)
st.rerun()