"""
使用python的pop3接口模块查看pop邮件账户的信息；这只是一个简单的列表查看软件
"""
import poplib, getpass, sys, mailconfig

mailserver = 'pop.qq.com'
mailuser = '******'
mailpasswd = 'hbptc******afagc'

print('Connecting...')
server = poplib.POP3_SSL(mailserver, '995')
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mail messages in', msgBytes, 'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')

    for i in range(msgCount):
        hdr, message, octets = server.retr(i+1)
        for line in message: print(line.decode())
        print('-' * 80)
        if i < msgCount - 1:
            input('[Press Enter key]')

finally:
    server.quit()

print('Bye.')































