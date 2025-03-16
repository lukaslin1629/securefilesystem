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
                user_db[un] = bytes.fromhex(hashed_pw) #returns as bytes correctly
    return user_db

# save a new user to the CSV file
def save_user(un, hashed_pw):
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([un, hashed_pw.hex()])  # Store as string

# register a new user
def register_user(user_db, un, pw):
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
def authenticate_user(user_db, un, pw):
    # check if un exists
    if un in user_db:
        # retrieve stored hashed pw
        stored_pw = user_db[un]
        
        # compare provided pw with stored hash
        if bcrypt.checkpw(pw.encode("utf-8"), stored_pw):
            print(f"User {un} logged in successfully.")
            return True
        else:
            print("Invalid password.")
    else:
        print("Username not found.")
    return False