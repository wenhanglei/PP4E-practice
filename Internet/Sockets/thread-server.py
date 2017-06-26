"""
Server side: open a socket on a port, listen for a message from a client, 
and send an echo replay; echoes lines until eof when client closes socket;
spawns a thread to handle each client connection; threads share global 
memory space with main thread; this is more portable than fork: threads
work on standard Windows systems, but process forks do not;
"""
# import socket
# import _thread
# from socket import AF_INET, SOCK_STREAM
# import time
#
# host = 'localhost'
# port = 50024
#
# slock = _thread.allocate_lock()
#
# def handler(conn, address):
#     info = conn.recv(2048)
#     time.sleep(3)
#     slock.acquire()
#     print('server received from '.encode() +
#           str(address[0]).encode() + ' '.encode() + str(address[1]).encode() +
#           info + ' '.encode())
#     conn.close()
#     slock.release()
#
# mysocket = socket.socket(AF_INET, SOCK_STREAM)
# mysocket.bind((host, port))
# mysocket.listen(5)
# while True:
#     conn, address = mysocket.accept()
#     _thread.start_new_thread(handler, (conn, address))

import time, _thread as thread
from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

def now():
    return time.ctime(time.time())

def handleClient(connection):
    time.sleep(5)
    while True:
        data = connection.recv(1024)
        if not data: break
        replay = 'Echo=>%s at %s' % (data, now())
        connection.send(replay.encode())
    connection.close()

def dispatcher():
    while True:
        connection, address = sockobj.accept()
        print('Server connected by', address, end=' ')
        print('at', now())
        thread.start_new_thread(handleClient, (connection,))

dispatcher()


















