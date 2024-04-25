import hashlib
import socket
import sys
import os

def initialization_server_socket(port):
    """ Initialization server socket """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen(1)
    print(f"Server listening on port {port}")
    return server_socket

def connection_with_client(server_socket):
    """ Handels the client request, and established connection with client"""
    connection, client_ip = server_socket.accept()
    print(f"Connected to client side from {client_ip}")

    # Receiving data from the client
    data_from_client = connection.recv(1024)
    print('Data received from client:', data_from_client)

    return connection, client_ip, data_from_client

def generate_and_send_file(connection):
    """ Create a file with random data, compute its checksum, and send it to the client. """
    file_path = 'server_side.txt'
    # Generate random 1 KB of data and write to a file
    with open(file_path, 'wb') as file:
        file.write(os.urandom(1024))

    # Calculate the MD5 checksum of the file
    checksum = hashlib.md5()
    with open(file_path, 'rb') as file:
        for data in iter(lambda: file.read(4096), b''):
            checksum.update(data)
    file_checksum = checksum.hexdigest()
    
    # Send checksum and file content to the client
    connection.sendall(file_checksum.encode() + b'\n')
    with open(file_path, 'rb') as file:
        connection.sendall(file.read())

    return file_checksum

def server_code(listening_port):
    """ Handel incoming connections and initialiazation of other functions"""
    server_socket = initialization_server_socket(int(listening_port))

    while True:
        connection, client_ip, data_from_client = connection_with_client(server_socket)
        
        if data_from_client:
            file_checksum = generate_and_send_file(connection)
            print(f"File sent to client {client_ip} with checksum: {file_checksum}")
            connection.close()

if __name__ == "__main__":
    server_port = sys.argv[1] if len(sys.argv) == 2 else 8000
    print(server_port)
    server_code(server_port)
