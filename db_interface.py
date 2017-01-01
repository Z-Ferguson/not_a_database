from database import Database
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
    taken_username = []
    with open("data.csv", "r") as f:
        for line in f:
            new_line = line.strip().split(",")
            taken_username.append(new_line[0])
    user_info = []
    name = input("Enter a user name: ")
    if name in taken_username:
        print("That username is taken")
        name = input("Enter a user name: ")
    else:
        user_info.append(name)
    password = input("Enter a password: ")
    user_info.append(password)
    phone = input("Please enter a phone number: ")
    user_info.append(phone)
    dob = input("Please enter your date of birth: ")
    user_info.append(dob)
    db.add(user_info)


def print_info(user_info):
    print("Your user infomation:")
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
        if check_user_name(user_name, user_dict) == True:
            print("Please enter password")
            password = get_input()
            checkp = check_password(user_name, user_dict, password)
            if checkp == True:
                user_info = user_dict[user_name]
                print_info(user_info)
            else:
                print("That info is not correct")
                continue
        else:
            print("That is not a current username. Please try again.")
            main()
        while True:
            print("Would you like to add a user? y/n.")
            user_choice = get_input().lower()
            accep_input = ['y', 'n']
            if user_choice not in accep_input:
                print("Please enter 'y' or 'n'.")
                user_choice = get_input().lower()
            elif user_choice == 'y':
                add_user()
            else:
                break

main()
