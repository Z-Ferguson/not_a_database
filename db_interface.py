from database import *

db = Database()
new_users = []

def get_input():
    ui = input(">")
    return ui

def check_user_name(username, user_dict):
    for key in user_dict:
        if user_name == key:
            return True

def main():
    user_dict = db_users
