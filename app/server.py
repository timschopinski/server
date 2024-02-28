import socket
from settings import HOST, PORT


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))

    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} has been established.")

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        message = data.decode('utf-8')
        print(f"Received message from client: {message}")

        response = f"Server received message: {message}"
        client_socket.send(response.encode('utf-8'))

    client_socket.close()


if __name__ == '__main__':
    start_server()