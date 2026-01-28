import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Migration Control Center", layout="wide")

st.title("🚀 Enterprise Microservices Migration Dashboard")
st.markdown("---")

# --- Service Status Logic ---
services = {
    "Access Control": "http://localhost:8000",
    "Entitlements": "http://localhost:8001",
    "Licensing": "http://localhost:8002",
    "Telemetry": "http://localhost:8003"
}

cols = st.columns(len(services))

for i, (name, url) in enumerate(services.items()):
    with cols[i]:
        try:
            # Try to hit the real service
            res = requests.get(url, timeout=0.5)
            status = "ONLINE" if res.status_code < 500 else "ERROR"
            st.success(f"**{name}**\n\n{status}")
        except:
            # Fallback to Demo Mode so it looks good for recruiters
            st.info(f"**{name}**\n\nDEMO MODE")

st.markdown("### 📊 Migration Performance Metrics")

# Mock data for charts
chart_data = pd.DataFrame({
    "Service": list(services.keys()),
    "Latency (ms)": [45, 120, 85, 30],
    "Uptime (%)": [99.9, 98.5, 99.2, 100.0]
})

col_a, col_b = st.columns(2)
with col_a:
    st.bar_chart(chart_data.set_index("Service")["Latency (ms)"])
    st.caption("Average Request Latency (Target: <200ms)")

with col_b:
    st.line_chart([0.1, 0.2, 0.1, 0.5, 0.2, 0.1])
    st.caption("Error Rate (%) - 24hr Window")
