#Name: Lukas Lin
#File Description: transfers the encrypted files from start to destination. fernet library is used
#           and the socket library is used to do file transfer.

import socket
from cryptography.fernet import Fernet
from .secure_client import compute_file_hash

#loads encryption key from secret.key
def load_key():
    return open("secret.key", "rb").read()

#decrypts file using fernet
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    #opens encrypted file to read contents
    with open(file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open("decrypted_" + file_name[:-4], "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"{file_name} decrypted successfully. ")

#server code
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create tcp socket
    server_socket.bind(('0.0.0.0', 65432)) #bind server to available interfaces
    server_socket.listen(1) #listen for incoming connections
    print("Server is listening for incoming connections...")

    #accept client connection
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    file_hash = conn.recv(64).decode('utf-8')  # SHA-256 hash is decoded
    print(f"Received file hash: {file_hash}")

    #open file to save received data
    with open("received_file.enc", "wb") as f:
        while True:
            data = conn.recv(1024) #receive data in 1024 byte chunks
            if not data:
                break
            f.write(data)
    #close the client connection
    conn.close()
    print("File received. Decrypting now...")

    received_file_hash = compute_file_hash("received_file.enc")
    print(f"Received file hash (computed): {received_file_hash}")

    # Verify file integrity
    if file_hash == received_file_hash:
        print("File integrity verified.")
    else:
        print("File integrity check failed: The file may be corrupted or tampered with.")

    #decrypt received file
    decrypt_file("received_file.enc")