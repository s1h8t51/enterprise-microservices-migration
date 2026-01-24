import time
from prometheus_client import start_http_server, Counter

# Define custom metrics
LICENSE_VALIDATION_TOTAL = Counter(
    'license_validation_total', 
    'Total number of license checks', 
    ['status']
)

def track_usage(status):
    """
    Increments the counter for Prometheus scraping.
    """
    LICENSE_VALIDATION_TOTAL.labels(status=status).inc()

if __name__ == "__main__":
    # Start Prometheus metrics endpoint
    start_http_server(8001)
    print("Telemetry exporter running on port 8001")
    while True:
        # Simulate tracking
        track_usage(status="success")
        time.sleep(5)
