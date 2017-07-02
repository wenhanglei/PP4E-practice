"""
测试连接标准流到socket.makefile的文本模式和二进制模式文件：print需要文本模式，但是文本模式
排除非缓存模式--需要使用-u参数和sys.stdout.flush()调用
"""
import sys

def reader(F):
    tmp, sys.stdin = sys.stdin, F
    line = input()
    print(line)
    sys.stdin = tmp

reader(open('test_stream_modes.py'))                     #input()返回文本
reader(open('test_stream_modes.py', 'rb'))               #input()返回二进制文件

def writer(F):
    tmp, sys.stdout = sys.stdout, F
    print(99, 'spam')
    sys.stdout = tmp

writer(open('temp', 'w'))
print(open('temp').read())

writer(open('temp', 'wb'))                           #打印错误，wb模式下无法打印str
writer(open('temp', 'w', 0))                         #打开错误， 无法打开非缓存模式的text文本






































