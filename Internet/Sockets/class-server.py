"""
Server side: open a socket on a port, listen for a messafe from a client, and
send an echo replay; this version uses the standard library module socketserver to 
do its work; socketserver provides TCPServer, ThreadingTCPServer, ForkingTCPServer, 
UDP variants of these, and more, and routes each client connect request to a new
instance of a passed-in request handler object's handle method; socketserver also 
supports Unix domain sockets, but only on Unixen; see the Python library manual.
"""

import socketserver, time
myHost = ''
myPort = 50007

def now():
    return time.ctime(time.time())

class MyclientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address,now())
        time.sleep(5)
        while True:
            data = self.request.recv(1024)
            if not data: break
            replay = 'Echo=>%s at %s' % (data, now())
            self.request.send(reply.encode())
        self.request.close()

    myaddr = (myHost, myPort)
    server = socketserver.ThreadingTCPServer(myaddr, MyclientHandler)
    server.serve_forever()































