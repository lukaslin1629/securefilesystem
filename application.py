import os
import sys
from secure_transfer.encrypt_decrypt import generate_key, encrypt_file, decrypt_file
from secure_transfer.secure_client import send_file
from secure_transfer.secure_server import start_server
from secure_transfer.authenticate import register_user, authenticate_user

def authentication_menu():
    """First menu: Handles user registration and login"""
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1": #password authentication system
            un = input("Enter a new username: ")
            pw = input("Enter a new password: ")
            register_user(un, pw)
            print("Registration successful. You can now log in.")
        elif choice == "2":
            un = input("Enter username: ")
            pw = input("Enter password: ")
            if authenticate_user(un, pw):
                print(f"Welcome, {un}!")
                main_menu(un)  #goes to main menu after authentication
            else:
                print("Invalid credentials. Try again.") #incorrect password
        elif choice == "3":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.") #incorrect input

def main_menu(un):
    """Second menu: Handles encryption, decryption, and file transfers after login"""
    while True:
        print(f"\nSecure File Transfer - Logged in as {un}")
        print("1. Generate Key") #generate the secret key
        print("2. Encrypt File") #encrypt new file without sending
        print("3. Decrypt File") #decrypt a file
        print("4. Start Server") #where the connections are handled
        print("5. Send File") #send file after server is opened
        print("6. Logout") #done!

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_name = input("Enter file name to encrypt: ")
            encrypt_file(file_name)
        elif choice == "3":
            file_name = input("Enter encrypted file name to decrypt: ")
            decrypt_file(file_name if file_name.endswith(".enc") else file_name + ".enc") #adds enc extension automatically
        elif choice == "4":
            print("Starting server...")
            start_server()
        elif choice == "5":
            file_name = input("Enter file name to send: ")
            if not file_name.endswith(".enc"): #adds enc extension if none
                encrypt_file(file_name)  #encrypt if not already encrypted
                file_name += ".enc"
            send_file(file_name)
        elif choice == "6":
            print("Logging out...")
            authentication_menu()  #return to login/register menu
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    authentication_menu()