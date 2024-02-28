import socket
from settings import HOST, PORT


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        message = input('Enter a message: ')
        if message == 'q':
            break
        client_socket.send(message.encode('utf-8'))

        response = client_socket.recv(1024)
        print(f"Received response from server: {response.decode('utf-8')}")

    client_socket.close()


if __name__ == '__main__':
    start_client()
