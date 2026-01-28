import streamlit as st
import requests

# Dictionary of your services and their "Website" (Documentation) URLs
# Use 127.0.0.1 for local testing, or your public Cloud URL for deployment
service_links = {
    "Access Control": "http://127.0.0.1:8000/docs",
    "Entitlements": "http://127.0.0.1:8001/docs",
    "Licensing": "http://127.0.0.1:8002/docs",
    "Telemetry": "http://127.0.0.1:8003/docs"
}

st.title("🚀 Enterprise Migration Control Center")
st.write("Click on a service name to view its API Documentation.")

cols = st.columns(len(service_links))

for i, (name, url) in enumerate(service_links.items()):
    with cols[i]:
        # This creates a clickable header
        st.markdown(f"### [{name}]({url})")
        
        try:
            # Check if the site is actually up
            # We use a 0.5s timeout so the dashboard doesn't lag
            res = requests.get(url.replace("/docs", ""), timeout=0.5) 
            if res.status_code < 400:
                st.success("Status: ONLINE")
            else:
                st.warning(f"Status: {res.status_code}")
        except:
            st.error("Status: OFFLINE")
