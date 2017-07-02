"""
###################################################################################
测试 socket的流重定向模块
###################################################################################
"""

import sys, os, multiprocessing
from socket_stream_redirect import *

###################################################################################
#重定向客户端输出
###################################################################################

def server1():
    mypid = os.getpid()
    conn = initListenerSocket()                           #阻塞直到客户端连接
    file = conn.makefile('r')
    for i in range(3):                                    #读取客户端的输出
        data = file.readline().rstrip()                   #阻塞直到数据准备好
        print('server %s got [%s]' % (mypid, data))       #输出文本到控制台

def client1():
    mypid = os.getpid()
    redirectOut()
    for i in range(3):
        print('cliend %s: %s' % (mypid, i))               #输出内容到socket
        sys.stdout.flush()                                #缓存直到退出

#############################################################################
# 重定向客户端输入
#############################################################################

def server2():
    mypid = os.getpid()                                     #原始socket未缓存
    conn = initListenerSocket()                             #发送到客户端的输入
    for i in range(3):
        conn.send(('server %s: %s\n' % (mypid, i)).encode())

def client2():
    mypid = os.getpid()
    redirectIn()
    for i in range(3):
        data = input()                                      #从socket接收的输入
        print('client %s got [%s]' % (mypid, data))         #正常打印到控制台

##############################################################################
# 重定向客户端的输入和输出
##############################################################################

def server3():
    mypid = os.getpid()
    conn = initListenerSocket()                           #等待客户端的连接
    file = conn.makefile('r')                             #接收客户端的输出，发送客的输入
    for i in range(3):
        data = file.readline().rstrip()
        conn.send(('server %s got [%s]\n' % (mypid, data)).encode())

def client3():
    mypid = os.getpid()
    redirectBothAsClient()
    for i in range(3):
        print('client %s: %s' % (mypid, i))                        #打印到socket
        data = input()                                             #获得来自socket的输入
        sys.stderr.write('client %s got [%s]\n' % (mypid, data))   #不重定向

##############################################################################
# 重定向客户端的输入和输出
##############################################################################

def server4():
    mypid = os.getpid()
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    for i in range(3):
        sock.send(('server %s: %s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))

def client4():
    mypid = os.getpid()
    redirectBothAsServer()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        sys.stdout.flush()

##########################################################################

def server5():
    mypid = os.getpid()
    conn = initListenerSocket()
    file = conn.makefile('r')
    for i in range(3):
        conn.send(('server %s: %s\n' % (mypid, i)).encode())
        data = file.readline().rstrip()
        print('server %s got [%s]' % (mypid, data))

def client5():
    mypid = os.getpid()
    s = redirectBothAsClient()
    for i in range(3):
        data = input()
        print('client %s got [%s]' % (mypid, data))
        sys.stdout.flush()

############################################################################
# 按数字用命令行测试
###########################################################################

if __name__ == '__main__':
    server = eval('server' + sys.argv[1])
    client = eval('client' + sys.argv[1])
    multiprocessing.Process(target=server).start()
    client()



































