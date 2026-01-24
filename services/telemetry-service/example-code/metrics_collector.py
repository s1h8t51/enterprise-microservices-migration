import time
from fastapi import FastAPI, BackgroundTasks
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI()

# 1. Define Prometheus Metrics
REQUEST_LATENCY = Histogram(
    "service_request_latency_seconds", 
    "Latency of service requests in seconds",
    ["service_name"]
)
EVENT_COUNT = Counter(
    "telemetry_events_total", 
    "Total number of telemetry events processed",
    ["event_type"]
)

# 2. Add Prometheus Scrape Endpoint
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.post("/v1/events", status_code=202)
async def ingest_event(data: dict, background_tasks: BackgroundTasks):
    """
    Ingests events asynchronously to ensure zero impact on the calling service's latency.
    """
    event_type = data.get("event_type", "unknown")
    
    # Increment Prometheus counter
    EVENT_COUNT.labels(event_type=event_type).inc()
    
    # Process the heavy lifting (DB write) in the background
    background_tasks.add_task(process_telemetry_data, data)
    
    return {"status": "accepted"}

def process_telemetry_data(data: dict):
    # This is where you would write to TimescaleDB or InfluxDB
    # print(f"Processing {data['event_type']} for {data['service_name']}")
    time.sleep(0.01)  # Simulate DB write
