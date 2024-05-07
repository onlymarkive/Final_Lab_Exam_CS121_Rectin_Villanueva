import json
import os
from user import User

class UserManager:

def __init__(self, filename="users.json"):
    self.filename = filename
    self.users = {}
    self.load_users()

def load_users(self):
    if os.path.exists(self.filename):
        with open(self.filename, "r") as f:
            user_list = json.load(f)
            for user_data inuser_list:
                user = User(**user_data)
                self.users[user.username] = user
    else: 
        with open(self.filename, "w") as f:
            json.dump([], f)

def save_users(self):
    with open(self.filename, "w") as f:
        json.dump ([user.__dict__ for user in self.users.values()], f)

def validate_user_name(self, username):
    return len(username) >= 4

def validate_user_password(self, password):
    return len(password) >= 8

def register():
    if not self.validate_username(username):
        return "Username must be at least 4 characters."
    if not self.validate_user_password(password):
        return "Password must be at least 8 characters."

    if username in self.users:
        return "Username already exists."

    user = User(username, password)
    self.users[username] = user
    self.save_users()
    return f"User{username} registered succcessfully"

def log_in(self, username, password):
    if username not inself.users:
        return "User not found."
    if self.users[username].password != password:
        return "Incorrect password."