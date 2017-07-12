"Display languages.py script code without running it."

import cgi, html
filename = 'cgi-bin/languages.py'

print('Content-type: text/html\n')
print('<TITLE>Languages</TITLE>')
print("<H1>Source code: '%s'</H1>" % filename)
print('<HR><PRE>')
print(html.escape(open(filename).read()))
print('</PRE><HR>')

















