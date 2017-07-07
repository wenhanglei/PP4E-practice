"""
用python实现一个简单的http服务器并且运行GCI脚本
"""
import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 80

if len(sys.argv) > 1: webdir = sys.argv[1]
if len(sys.argv) > 2: port = int(sys.argv[2])
print('webdir "%S", port %s' % (webdir, port))

os.chdir(webdir)
srvraddr = ('', port)
srvrobj = HTTPServer(srvraddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()

































