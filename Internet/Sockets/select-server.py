"""
Server: handle multiple clients in parallel with select. use the select
module to manually multiplex among a set of sockets: main sockets which 
accept new client connections, and input sockets connected to accepted 
clients; select can take an optional 4th arg--0 to poll, n.m to wait n.m 
seconds. or omitted to wait till any socket is ready for processing.
"""

import sys, time
from select import select
from socket import socket, AF_INET, SOCK_STREAM
def now(): return time.ctime(time.time())

myHost = ''
myPort = 50007
if len(sys.argv) == 3:
    myHost, myPort = sys.argv[1:]
numPortSocks = 2

mainsocks, readsocks, writesocks = [], [], []
for i in range(numPortSocks):
    portsock = socket(AF_INET, SOCK_STREAM)
    portsock.bind((myHost, myPort))
    portsock.listen(5)
    mainsocks.append(portsock)
    readsocks.append(portsock)
    myPort += 1

print('select-server loop starting')
while True:
    readables, writeables, exceptions = select(readsocks, writesocks, [])
    for sockobj in readables:
        if sockobj in mainsocks:
            newsock, address = sockobj.accept()
            print('Connect:', address, id(newsock))
            readsocks.append(newsock)
        else:
            data = sockobj.recv(1024)
            print('\tgot', data, 'on', id(sockobj))
            if not data:
                sockobj.close()
                readsocks.remove(sockobj)
            else:
                reply = 'Echo=>%s at %s' % (data, now())
                sockobj.send(reply.encode())






























