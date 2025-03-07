#Name: Lukas Lin
#File Description: transfers the encrypted files from start to destination. fernet library is used
#           and the socket library is used to do file transfer.

import socket
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as encrypted file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open("decrypted_" + file_name[:-4], "wb") as decrypted file:
        decrypted_file.write(decrypted_data)

    print(f"{file_name} decrypted successfully. ")

#server code
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 65432))
    server_socket.listen(1)
    print("Server is listening for incoming connections...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    with open("received_file.enc", "wb") as f:
        while True:
            data = connn.recv(1024)
            if not data:
                break
            f.write(data)
    
    conn.close()
    print("File received. Decrypting now...")
    decrypt_file("received_file.enc")

if __name__ == "__main__":
    start_server()