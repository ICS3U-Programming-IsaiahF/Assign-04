#!/usr/bin/env python3

# Created by: Isaiah Fernandez
# Date: January 11, 2023
# This program lets the user make their password and enter it again to check if it is the right password.

import getpass
import time

def main():
    while True:
        password_one = getpass.getpass("Make your password: ")
        for char in password_one:
            print(char, end="", flush=True)
            time.sleep(0.2)
            print("\b*", end="", flush=True)
        print("")
        confirmed_password = getpass.getpass("Confirm your password: ")
        for char in confirmed_password:
            print(char, end="", flush=True)
            time.sleep(0.2)
            print("\b*", end="", flush=True)
        print("")
        if password_one == confirmed_password:
            break
        else:
            print("The passwords do not match. \nEnter new password.\n")

    while True:
        attempt = getpass.getpass("Enter your password: ")
        for char in attempt:
            print(char, end="", flush=True)
            time.sleep(0.2)
            print("\b*", end="", flush=True)
        print("")
        if attempt == confirmed_password:
            print("Password is correct!")
            break
        else:
            print("Incorrect password. Please try again.")

if __name__ == "__main__":
    main()
