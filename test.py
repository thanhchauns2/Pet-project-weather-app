from Infra.SQLiteConnector import SQLiteConnector
from Business.Entity.Accounts import Accounts
from Business.Constants import Constants
import sqlite3
from Controller.controller import notify_weather

# # Create table if not exists
# conn = sqlite3.connect(Constants.ACCOUNTS_DB_PATH)
# cursor = conn.cursor()
# cursor.execute(f"""
# CREATE TABLE IF NOT EXISTS {Constants.ACCOUNTS_TABLE_NAME} (
#     account_username TEXT PRIMARY KEY,
#     account_password TEXT,
#     email TEXT,
#     latitude REAL,
#     longitude REAL,
#     account_type TEXT
# )
# """)
# conn.commit()

# # Create sample accounts
# accounts = [ # You can add your own accounts here for testing
#     Accounts("admin1", "admin1", "abc@gmail.com", 35.6762, 139.6503, "admin"),
#     Accounts("adam123", "adam123", "adam123@gmail.com", 51.5074, -0.1278, "user"),
# ]

# # Add accounts to database
# db = SQLiteConnector(conn)
# for account in accounts:
#     try:
#         db.add_account(account)
#     except sqlite3.IntegrityError:
#         print(f"Account {account.account_username} already exists")

# conn.close()

conn = sqlite3.connect(Constants.ACCOUNTS_DB_PATH)
notify_weather(conn)
conn.close()

