"""
sockets for cross-task communication: start threads to communicate over sockets;
independent programs can too, because sockets are system-wide, much like fifos;
see the GUI and Internet parts of the book for more realistic socket use cases;
some socket servers may also need to pickled objects or encoded Unicode text;
caveat: prints in threads may need to be synchronized if their output overlaps;
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading

host = 'localhost'
port = 50008

def server():
    sock = socket(AF_INET, SOCK_STREAM)            #ip adress and TCP connection
    sock.bind('', port)                            #bind connection with local machine
    sock.listen(5)                                 #最多同时监听5个客户端的请求
    while True:
        conn, addrs = sock.accept()
        msg = conn.recv(1024)
        reply = '[%s] was received' % msg
        conn.send(reply.encode())

def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(host, port)
    sock.send(name.encode())
    reply = sock.recv(1024)
    socket.close()
    print('client got: [%s]' % reply)

if __name__ == '__main__':
    sthread = threading.Thread(target=server, args=())
    sthread.start()
    sthread.daemon = True
    for i in range(5):
        name = 'client%s' % i
        threading.Thread(target=client, args=(name,)).start()



































