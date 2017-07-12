"""
主页面和回复页面公用的通用对象；
只需要修改这个文件就可以添加新语言
"""

inputkey = 'language'

hellos = {
    'Python': r" print('Hello World') ",
    'Python2': r" print 'Hello World' ",
    'Perl': r' print "Hello World\n"; ',
    'Tcl': r' puts "Hello World" ',
    'Scheme': r' (display "Hello World") (newline) ',
    'SmallTalk': r" 'Hello World' print. ",
    'Java': r' System.out.println("Hello World"); ',
    'C': r' printf("Hello World\n"); ',
    'C++': r' cout << "Hello World" << endl; ',
    'Basic': r' 10 PRINT "Hello World" ',
    'Fortran': r" print *, 'Hello World' ",
    'Pascal': r" WriteLn('Hello World'); "
}