import sqlite3
from Business.Constants import Constants
from Business.Entity.Accounts import Accounts
class SQLiteConnector:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.cursor = self.conn.cursor()
    
    def get_accounts(self):
        self.conn = sqlite3.connect(Constants.ACCOUNTS_DB_PATH)
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (Constants.ACCOUNTS_TABLE_NAME,))
        table_name = self.cursor.fetchone()[0]
        if table_name is None:
            raise Exception(f"Table {Constants.ACCOUNTS_TABLE_NAME} does not exist")
        self.cursor.execute(f"SELECT * FROM {Constants.ACCOUNTS_TABLE_NAME}")
        result = self.cursor.fetchall()
        self.conn.close()
        return result
    
    def add_account(self, account: Accounts):
        self.cursor.execute(f"INSERT INTO {Constants.ACCOUNTS_TABLE_NAME} (account_username, account_password, email, latitude, longitude, account_type) VALUES (?, ?, ?, ?, ?, ?)", (account.account_username, account.account_password, account.email, account.latitude, account.longitude, account.account_type))
        self.conn.commit()
        
    def update_account(self, account: Accounts):
        self.cursor.execute(f"UPDATE {Constants.ACCOUNTS_TABLE_NAME} SET account_password = ?, email = ?, latitude = ?, longitude = ?, account_type = ? WHERE account_username = ?", (account.account_password, account.email, account.latitude, account.longitude, account.account_type, account.account_username))
        self.conn.commit()
    
    def delete_account(self, account_username: str):
        self.cursor.execute(f"DELETE FROM {Constants.ACCOUNTS_TABLE_NAME} WHERE account_username = ?", (account_username,))
        self.conn.commit()

    def execute(self, query: str, params: tuple = ()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetchone(self):
        return self.cursor.fetchone()

