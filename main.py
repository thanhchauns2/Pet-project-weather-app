from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Controller.controller import notify_weather, URLS
from Controller.DTO import create_routes
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3
from Business.Constants import Constants

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_routes(app, URLS)

conn = sqlite3.connect(Constants.ACCOUNTS_DB_PATH)
scheduler = BackgroundScheduler()
scheduler.add_job(notify_weather, 'cron', minute=55, args=[conn])
scheduler.start()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
