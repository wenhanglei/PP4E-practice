"""
#################################################################################
使用Python的SMTP模块的接口发送邮件信息
#################################################################################
"""

import smtplib, sys, email.utils, mailconfig
mailserver = mailconfig.smtpservername

From = input('From? ').strip()
To   = input('To?   ').strip()
Tos  = To.split(';')
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()

text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d , Ctrl+z]')
while True:
    line = sys.stdin.readline()
    if not line:
        break
    text += line

print('Connecting...')
server = smtplib.SMTP(mailserver)
failed = server.sendmail(From, Tos, text)
server.quit()
if failed:
    prnt('Failed recipients:', failed)
else:
    print('No errors.')
print('Bye')

































