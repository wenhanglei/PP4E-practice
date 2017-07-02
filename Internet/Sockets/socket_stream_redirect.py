import sys
from socket import *
port = 50008
host = 'localhost'

def initListenerSocket(port=port):
    """
    初始化以服务端模式监听调用函数的连接socket
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(('', port))
    sock.listen(5)
    conn, addr = sock.accept()
    return conn

def redirectOut(port=port, host=host):
    """
    连接调用函数的输出流到为GUI监听的socket，调用函数必须在监听器启动后调用，否则会失败
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))                         #调用函数运行在客户端模式下
    file = sock.makefile('w')                          #文件接口: 文本， 带缓存
    sys.stdout = file                                  #使print连接到sock.send函数
    return sock                                        #如果调用函数需要访问原始socket

def redirectIn(port=port, host=host):
    """
    连接调用函数的标准输入流到GUI的输入socket 
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r')
    sys.stdin = file                          #文件接口包装器
    sys.stdin = file                          #连接input和sock.recv
    return sock                               #该返回值可以忽略

def redirectBothAsClient(port=port, host=host):
    """
    连接调用函数的标准输入流和输出流到同一个socket的模式，调用函数是一个
    服务器的客户端：发送消息，接受回复
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))                    #可以以'rw'模式打开
    ofile = sock.makefile('w')                    #文件接口
    ifile = sock.makefile('r')                    #包装同一个socket的两个文件对象
    sys.stdout = ofile                            #关联print和sock.send
    sys.stdin = ifile                             #关联input和sock.recv
    return sock

def redirectBothAsServer(port=port, host=host):
    """
    连接调用函数的标准输入和标准输出流到同一个socket的模式，调用函数是一个
    客户端的服务器： 接受消息， 发送回复
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port))                      #调用函数在这里是一个监听器
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w')                   #文件接口包装器
    ifile = conn.makefile('r')                   #同一个socket包装的两个文件对象
    sys.stdout = ofile                           #关联print和sock.send
    sys.stdin = ifile                            #关联input和sock.recv
    return conn





























