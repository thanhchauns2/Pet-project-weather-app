from Business.Services.DailyNotifier import DailyNotifier
from Business.Services.HourlyNotifier import HourlyNotifier
from Business.Entity.WeatherForecaster import WeatherForecaster
from Business.Services.NotificationService import NotificationService
from Business.Entity.AccountManager import AccountsManager
from Business.Constants import Constants
import sqlite3
def notify_daily_weather(accounts, notification_service):
    from datetime import datetime
    current_hour = datetime.now().hour
    if current_hour != 6:
        return
    daily_notifier = DailyNotifier(WeatherForecaster())
    for account in accounts:
        notification_service.send_daily_weather_notification(account.email, account.latitude, account.longitude, daily_notifier)

def notify_hourly_weather(accounts, notification_service):
    hourly_notifier = HourlyNotifier(WeatherForecaster())
    for account in accounts:
        notification_service.send_hourly_weather_notification(account.email, account.latitude, account.longitude, hourly_notifier)

def notify_weather(conn: sqlite3.Connection):
    
    accounts_manager = AccountsManager(conn)
    accounts_manager.fetch_from_db()
    accounts = accounts_manager.get_all_accounts()
    
    notification_service = NotificationService(
        smtp_server=Constants.SMTP_SERVER,
        smtp_port=Constants.SMTP_PORT,
        sender_email=Constants.SENDER_EMAIL,
        sender_password=Constants.SENDER_PASSWORD
    )
    
    notify_daily_weather(accounts, notification_service)
    notify_hourly_weather(accounts, notification_service)

def index():
    return "Hello World"

URLS = [
    ('GET', '/index', index)
]