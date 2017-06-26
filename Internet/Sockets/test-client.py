from socket import socket, AF_INET, SOCK_STREAM

info = b'gan ni ma'
host = 'localhost'
port = 50024

c_socket = socket(AF_INET, SOCK_STREAM)
c_socket.connect((host, port))
c_socket.send(info)