from socket import *
sock = socket()
sock.bind(('', 60000))
sock.listen(5)
print('accepting...')
conn, id = sock.accept()

for i in range(3):
    print('receiving...')
    msg = conn.recv(1024)
    print(msg)






























