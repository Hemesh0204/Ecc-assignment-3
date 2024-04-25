import socket
import hashlib
import sys

def get_checksum(connection_socket):
    # Get the checksum code from server
    received_checksum = connection_socket.recv(33).decode().strip()
    print("Received checksum from server:", received_checksum)

    with open("client_side.txt", "wb") as output_file:
        while True:
            file_data = connection_socket.recv(1024)
            if not file_data:
                break
            output_file.write(file_data)
    return received_checksum

def calc_checksum(filename):
    # Calculating the checksum value using the md5 algorithm
    file_hasher = hashlib.md5()
    with open(filename, "rb") as file:
        for data_chunk in iter(lambda: file.read(4096), b""):
            file_hasher.update(data_chunk)
    return file_hasher.hexdigest()

def connect_to_server(server_address, server_port):
    # Connecting to the server
    try:
        connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection_socket.connect((server_address, int(server_port)))
        connection_socket.sendall(b"Yo Server, ig we got connected")

        received_checksum = get_checksum(connection_socket)
        computed_checksum = calc_checksum("client_side.txt")
        
        print("Checksum computed at client side:", computed_checksum)

        # Check whether the checksum values are correct or not
        if computed_checksum == received_checksum:
            print(f"Checksum is correct and the file is received: {computed_checksum}")
        else:
            print(f"Checksum mismatch: expected {received_checksum}, got {computed_checksum}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection_socket.close()

if __name__ == "__main__":
    # Default server address and port or get from command line arguments
    server_address = sys.argv[1] if len(sys.argv) == 3 else "172.17.0.2"
    server_port = sys.argv[2] if len(sys.argv) == 3 else 8000
    connect_to_server(server_address, server_port)

