import socket
import hashlib
from cryptography.fernet import Fernet

#loads encryption key from secret.key file
def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)
    
    #read original file data
    with open(file_name, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)
    
    #save encrypted data to new .enc file
    with open(file_name + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    print(f"{file_name} encrypted successfully.")

#computes SHA-256 hash
def compute_file_hash(file_name):
    sha256_hash = hashlib.sha256()
    with open(file_name, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

#sends file over tcp connection
def send_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 65432))

    client_socket.sendall(file_hash.encode('utf-8'))

    #opens file and sends contents
    with open(file_name, "rb") as f:
        data = f.read()
        client_socket.sendall(data)

    #closes socket connection 
    print("File sent successfully.")
    client_socket.close()