#Name: Lukas Lin
#File Description: encypting/decrypting the files

#note: Encryption Algorithm: Fernet uses AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode for encryption and HMAC-SHA256 for authentication.
#      Uses HMAC(Hash-based Message Authetication Code).

from cryptography.fernet import Fernet
import os

#generate key and save to file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

#load key from file
def load_key():
    return open("secret.key", "rb").read()

#encrypt file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
      encrypted = encrypted_file.read()
    
    decrypted = fernent.decrypt(encrypted)

    with open("decrypted_" + encrypted_file_name[:-4]. "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"{encrypted_file_name} has been deecrypted to decrypted_{encrypted_file_name[:-4]}")

#option input
def main():
    While True:
        print("\n1. Generate Key\n2. Encrypt File\n3. Decrypt File\n4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            generate_key()
        elif choice == '2':
            file_name = input("Enter the file name to encrypt: ")
            encrypt_file(file_name)
        elif choice == '3':
            encrypted_file_name = input("Enter the encrypted file name to decrypt: ")
            decrypt_file(encrypted_file_name)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Enter a value 1-4.")

if __name__ == "__main__":
    main()