from fastapi import FastAPI
import os
import psycopg2
from datetime import datetime

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://admin:Berlin@db:5432/app_db"
)

def get_connection():
    return psycopg2.connect(DATABASE_URL)

@app.on_event("startup")
def startup():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

@app.get("/")
def read_root():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO visits DEFAULT VALUES")
    cur.execute("SELECT COUNT(*) FROM visits")
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Hello Docker Compose!", "visits": count}
