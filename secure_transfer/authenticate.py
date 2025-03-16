#Project: Encrypting a Filesystem (Learning Cybersecurity)
#Name: Lukas Lin
#File Description: Authentication system for user logins

import csv
import bcrypt
import os

# CSV file to store user data
CSV_FILE = "users.csv"

# load users from CSV file
def load_users():
    user_db = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                un, hashed_pw = row
                user_db[un] = hashed_pw.encode("utf-8")
    return user_db

# save a new user to the CSV file
def save_user(un, hashed_pw):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([un, hashed_pw.decode("utf-8")])  # Store as string

# register a new user
def reg_user(user_db, un, pw):
    # generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(pw.encode("utf-8"), salt)
    
    # store username and pw in the user_db
    if un in user_db:
        print("User already exists.")
    else:
        user_db[un] = hashed_pw
        save_user(un, hashed_pw)  # Save to CSV
        print(f"User {un} registered successfully.")

# authenticate user
def login_user(user_db, un, pw):
    # check if un exists
    if un in user_db:
        # retrieve stored hashed pw
        stored_pw = user_db[un]
        
        # compare provided pw with stored hash
        if bcrypt.checkpw(pw.encode("utf-8"), stored_pw):
            print(f"User {un} logged in successfully.")
        else:
            print("Invalid password.")
    else:
        print("Username not found.")

# command-line interface for testing
"""def main():
    user_db = load_users()  # load users from CSV file
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            un = input("Enter username: ")
            pw = input("Enter password: ")
            reg_user(user_db, un, pw)
        elif choice == "2":
            un = input("Enter username: ")
            pw = input("Enter password: ")
            login_user(user_db, un, pw)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
"""