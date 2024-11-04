from Infra.SQLiteConnector import SQLiteConnector
from Business.Entity.Accounts import Accounts
import hashlib

class AccountService:
    def __init__(self):
        pass
    
    def encrypt_password(self, account_password: str):
        encrypted_password = hashlib.sha256(account_password.encode()).hexdigest()
        return encrypted_password
    
    def authenticate(self, account_username: str, account_password: str):
        encrypted_password = self.encrypt_password(account_password)
        accounts = SQLiteConnector().get_accounts()
        for account in accounts:
            if account[1] == account_username and account[2] == encrypted_password:
                return True
        return False

    def register(self, account_username: str, account_password: str, email: str, latitude: float, longitude: float, account_type: str):
        account = Accounts(account_username, self.encrypt_password(account_password), email, latitude, longitude, account_type)
        SQLiteConnector().add_account(account)
    
    def update(self, account_username: str, account_password: str, email: str, latitude: float, longitude: float, account_type: str):
        account = Accounts(account_username, self.encrypt_password(account_password), email, latitude, longitude, account_type)
        SQLiteConnector().update_account(account)

    def delete(self, account_username: str):
        SQLiteConnector().delete_account(account_username)
