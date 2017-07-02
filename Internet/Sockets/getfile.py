"""
#################################################################################
实现通过socket从服务端传输任意文件到客户端的逻辑；使用简单的控制信息协议而不是分别用来控制和传输数据
的sockets，转发每个客户端的请求到处理器线程，循环传输文件块。
"""
import sys, os, time, _thread as thread
from socket import *

blksz = 1024
defaultHost = 'localhost'
defaultPort = 50001

helptext = """
server=> getfile.py -mode server              [-port nnn] [-host hhh|localhost]
client=> getfile.pay [-mode client] -file fff [-port nnn] [-host hhh|localhost]
"""

def now():
    return time.asctime()

def parsecommandline():
    dict = {}                             #放入dictionary方便查找
    args = sys.argv[1:]
    while len(args) >= 2:
        dict[args[0]] = args[1]
        args = args[2:]
    return dict

def client(host, port, filename):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    sock.send((filename + '\n').encode())           #发送远程主机的name
    dropdir = os.path.split(filename)[1]
    file = open(dropdir, 'wb')
    while True:
        data = sock.recv(blksz)
        if not data: break
        file.write(data)
    sock.close()
    file.close()
    print('Client got', filename, 'at', now())

def serverthread(clientsock):
    sockfile = clientsock.makefile('r')
    filename = sockfile.readline()[:-1]
    try:
        file = open(filename, 'rb')
        while True:
            bytes = file.read(blksz)
            if not bytes: break
            sent = clientsock.send(bytes)
            assert sent == len(bytes)
    except:
        print('Error downloading file on server:', filename)
    clientsock.close()

def server(host, port):
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.bind((host, port))
    serversock.listen(5)
    while True:
        clientsock, clientaddr = serversock.accept()
        print('Server connected by', clientaddr, 'at', now())
        thread.start_new_thread(serverthread, (clientsock,))

def main(args):
    host = args.get('-host', defaultHost)
    port = int(args.get('-port', defaultPort))
    if args.get('-mode') == 'server':
        if host == 'localhost': host = ''
        server(host, port)
    elif args.get('-file'):
        client(host, port, args['-file'])
    else:
        print(helptext)

if __name__ == '__main__':
    args = parsecommandline()
    main(args)




































