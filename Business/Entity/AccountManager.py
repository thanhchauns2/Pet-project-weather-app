from Infra.SQLiteConnector import SQLiteConnector
from Business.Entity.Accounts import Accounts
import sqlite3

class AccountsManager:
    def __init__(self, conn: sqlite3.Connection):
        self.accounts = []
        self.conn = conn
    
    def get_all_accounts(self):
        return self.accounts

    def fetch_from_db(self):
        self.accounts = SQLiteConnector(self.conn).get_accounts()
        self.accounts = [Accounts(account[0], account[1], account[2], account[3], account[4], account[5]) for account in self.accounts]