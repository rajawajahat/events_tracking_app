import socket


def socket_client(message):
    host = "localhost"
    port = 8080

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(message.encode())
    client_socket.close()
