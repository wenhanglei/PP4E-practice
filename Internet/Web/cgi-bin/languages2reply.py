"""
功能和language.py一样，但是更容易维护，使用HTML模版，从common模块获取
language表和输入健，从mockup获得可重用的测试数据
"""

import cgi, sys
from formMockup import FieldMockup
from languages2common import hellos, inputkey
debugme = False

hdrhtml = """Content-type: text/html\n
<TITLE> Languages</TITLE>
<H1>Syntax</H1><HR>
"""

langhtml = """
<H3>%s</H3><p><PRE>
%s
</PRE></P><BR>
"""

def showHello(form):
    choice = form[inputkey].value
    try:
        print(langhtml % (cgi.escape(choice),
                          cgi.escape(hellos[choice])))
    except KeyError:
        print(langhtml % (cgi.escape(choise),
                          "Sorry--I don't know that language"))

def main():
    if debugme:
        form = {inputekey: FieldMockup(sys.argv[1])}
    else:
        form = cgi.FieldStorage()

    print(hdrhtml)
    if not inputkey in form or form[inputkey].value == 'All':
        for lang in hellos.keys():
            mock = {inputkey: FieldMockup(lang)}
            showHello(mock)
    else:
        showHello(form)
    print('<HR>')

if __name__ == '__main__':
    main()



























