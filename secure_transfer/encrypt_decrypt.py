#Name: Lukas Lin
#File Description: encypting/decrypting the files

#note: Encryption Algorithm: Fernet uses AES (Advanced Encryption Standard) in CBC (Cipher Block Chaining) mode for encryption and HMAC-SHA256 for authentication.
#      Uses HMAC(Hash-based Message Authetication Code).
from cryptography.fernet import Fernet

# generate and save encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to secret.key")

# load key from file
def load_key():
    return open("secret.key", "rb").read()

# encrypt file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)

    with open(file_name + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"{file_name} has been encrypted to {file_name}.enc")

# decrypt file
def decrypt_file(encrypted_file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read() #read encrypted file

    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_name = "decrypted_" + encrypted_file_name[:-4]  # removes ".enc"
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"{encrypted_file_name} has been decrypted to {decrypted_file_name}")