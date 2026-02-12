mport asyncio
import httpx
import sqlite3
from datetime import datetime
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from typing import List

app = FastAPI(title="High-Availability Monitor")

# --- DATABASE SETUP (SQL Mastery) ---
DB_PATH = "health_checks.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS monitored_services (
                url TEXT PRIMARY KEY,
                fail_count INTEGER DEFAULT 0,
                last_status INTEGER,
                last_check TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS health_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT,
                status_code INTEGER,
                timestamp TIMESTAMP
            )
        """)
init_db()

# --- MODELS ---
class ServiceRegister(BaseModel):
    url: HttpUrl

# --- ASYNC ENGINE ---
async def check_url(client: httpx.AsyncClient, url: str):
    try:
        response = await client.get(url, timeout=5.0)
        status_code = response.status_code
    except Exception:
        status_code = 0

    # Persistence Logic
    with sqlite3.connect(DB_PATH) as conn:
        if status_code != 200:
            conn.execute("UPDATE monitored_services SET fail_count = fail_count + 1 WHERE url = ?", (url,))
            # Check for Critical Alert
            cursor = conn.execute("SELECT fail_count FROM monitored_services WHERE url = ?", (url,))
            fails = cursor.fetchone()[0]
            if fails >= 3:
                print(f"CRITICAL ALERT: {url} has failed {fails} times!")
        else:
            conn.execute("UPDATE monitored_services SET fail_count = 0 WHERE url = ?", (url,))
        
        conn.execute("UPDATE monitored_services SET last_status = ?, last_check = ? WHERE url = ?", 
                     (status_code, datetime.now(), url))
        conn.execute("INSERT INTO health_logs (url, status_code, timestamp) VALUES (?, ?, ?)", 
                     (url, status_code, datetime.now()))

async def monitoring_loop():
    """The background engine running every 30 seconds"""
    while True:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.execute("SELECT url FROM monitored_services")
            urls = [row[0] for row in cursor.fetchall()]
        
        if urls:
            async with httpx.AsyncClient() as client:
                tasks = [check_url(client, url) for url in urls]
                await asyncio.gather(*tasks)
        
        print(f"Loop completed at {datetime.now()}. Sleeping 30s...")
        await asyncio.sleep(30)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(monitoring_loop())

# --- ENDPOINTS ---
@app.post("/register")
async def register_service(service: ServiceRegister):
    with sqlite3.connect(DB_PATH) as conn:
        try:
            conn.execute("INSERT INTO monitored_services (url) VALUES (?)", (str(service.url),))
            return {"message": f"Now monitoring {service.url}"}
        except sqlite3.IntegrityError:
            return {"message": "Already monitoring this URL"}

@app.get("/status")
async def get_all_status():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute("SELECT * FROM monitored_services")
        return [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
