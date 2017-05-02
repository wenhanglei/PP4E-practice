"""
客户端
"""
from socket import socket, AF_INET, SOCK_STREAM

host = '127.0.0.1'
port = 2048

mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.connect((host, port))

msg = '这只是一个测试！'
mysocket.send(msg.encode())
newmsg = mysocket.recv(2048)
print(newmsg.decode())