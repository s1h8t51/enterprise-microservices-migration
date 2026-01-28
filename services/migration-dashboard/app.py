import streamlit as st
import requests

st.title("🚀 Enterprise Migration Control Center")

# Create columns for your 4 services
col1, col2, col3, col4 = st.columns(4)

services = {
    "Entitlements": "http://localhost:8000/v1/users/user_1/features",
    "Licensing": "http://localhost:8001/v1/validate?license_key=PRO-123",
    "Telemetry": "http://localhost:8002/metrics",
    "Access": "http://localhost:8003/v1/validate"
}

for col, (name, url) in zip([col1, col2, col3, col4], services.items()):
    with col:
        try:
            # Check if service is alive
            response = requests.get(url, timeout=1)
            if response.status_code < 400:
                st.success(f"{name}: ONLINE")
            else:
                st.warning(f"{name}: {response.status_code}")
        except:
            st.error(f"{name}: OFFLINE")

st.divider()
st.subheader("System Health Metrics")
# You could add charts here showing the 2% error rate alerts we built!
