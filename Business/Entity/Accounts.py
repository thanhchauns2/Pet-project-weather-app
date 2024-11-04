class Accounts:
    
    def __init__(self, account_username: str, account_password: str, email: str, latitude: float, longitude: float, account_type: str):
        self.account_username = account_username
        self.account_password = account_password
        self.email = email
        self.latitude = latitude
        self.longitude = longitude
        self.account_type = account_type

    def __str__(self):
        return f"Account Username: {self.account_username}, Account Password: {self.account_password}, Account Type: {self.account_type}, Email: {self.email}, Latitude: {self.latitude}, Longitude: {self.longitude}"


