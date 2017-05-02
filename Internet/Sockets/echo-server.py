"""
服务端： 打开TCP/IP socket 在一个端口， 监听来自客户端的信息，然后回传
"""
from socket import socket, AF_INET, SOCK_STREAM

host = ''
port = 2048

mysocket = socket(AF_INET, SOCK_STREAM)
mysocket.bind((host, port))

while True:
    mysocket.listen(5)
    conn, address = mysocket.accept()
    data = conn.recv(2048)
    reply = 'server receives the msg: %s' % data.decode()
    conn.send(reply.encode())
    conn.close()

