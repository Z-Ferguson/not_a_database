from database import *
import sys
import os

db = Database()
new_users = []

def get_input():
    ui = input(">")
    return ui


def check_user_name(user_name, user_dict):
    for key in user_dict:
        if user_name == key:
            return True


def check_password(user_name, user_dict, password):
    user_pass = user_dict[user_name][1]
    if password == user_pass:
        return True


def add_user():
    user_info = []
    name = input("Enter a user name: ")
    user_info.append(name)
    password = input("Enter a password: ")
    user_info.append(password)
    phone = input("Please enter a phone number: ")
    user_info.append(phone)
    dob = input("Please enter your date of birth: ")
    user_info.append(dob)
    db.add(user_info)
    main()


def print_info(user_info):
    print("Here is your user infomation:")
    print("Username:  {},  password:  {},  Phone:  {},  DOB: {}".format(user_info[0], user_info[1], user_info[2], user_info[3]))


def main():
    user_dict = db.users
    print("Welcome to Not a Database!")
    while True:
        print("Please enter your user name or enter 'q' to quit.")
        user_name = get_input()
        if user_name == 'q':
            exit()
        check = check_user_name(user_name, user_dict)
        if check_user_name(user_name,user_dict) == True:
            print("Please enter password")
            password = get_input()
            checkp = check_password(user_name,user_dict, password)
            if checkp == True:
                user_info = user_dict[user_name]
                print_info(user_info)
            else:
                print("That info is not correct")
                main()
        else:
            print("That is not a current username. Please try again.")

        print("Would you like to add a user? y/n")
        user_choice = get_input().lower()
        if user_choice == 'y':
            add_user()
        elif user_choice == 'n':
            main()

main()
