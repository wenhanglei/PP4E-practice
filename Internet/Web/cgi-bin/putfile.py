"""
####################################################################################
提取浏览器通过http上传的文件

caveat: could open output file in text mode to write receiving platform's line
ends since file content always str from the cgi module, but this is a temporary
solution anyhow--the cgi module doesn't handle binary file uploads;
#####################################################################################
"""
import cgi, os, sys
import posixpath, ntpath, macpath
debugmode = False
loadtextauto = False
uploaddir = './uploads'

sys.stderr = sys.stdout
form = cgi.FieldStorage()
print("Content-type: text/html\n")
if debugmode: cgi.print_form(form)

html = """
<html><title>Putfile response page</title>
<body>
<h1>Putfile response page</h1>
%s
</body></html>
"""

goodhtml = html % """
<p>Your file, '%s', has been saved on the server as '%s'.</p>
<p>An echo of the file's contents received and saved appears below.</p>
<hr>
<p><pre>%s</pre>
</p><hr>
"""

def splitpath(origpath):
    for pathmodule in [posixpath, ntpath, macpath]:
        basename = pathmodule.split(origpath)[1]
        if basename != origpath:
            return basename
    return origpath

def saveonserver(fileinfo):
    basename = splitpath(fileinfo.filename)
    srvrname = os.path.join(uploaddir, basename)
    srvrfile = open(srvrname, 'wb')
    if loadtextauto:
        filetext = fileinfo.value
        if isinstance(filetext, str):
            filedata = filetext.encode()
        srvrfile.write(filedata)
    else:
        numlines, filetext = 0, ''
        while True:
            line = fileinfo.file.readline()
            if not line: break
            if isinstance(line, str):
                line = line.encode()
            srvrfile.write(line)
            filetext +=line.decode()
            numlines += 1
        filetext = ('[Lines=%d]\n' % numlines) + filetext
    srvrfile.close()
    os.chmod(srvrname, 0o666)
    return filetext, srvrname

def main():
    if not 'clientfile' in form:
        print(html % 'Error: no file was received')
    elif not form['clientfile'].filename:
        print(html % 'Error: filename is missing')
    else:
        fileinfo = form['clientfile']
        try:
            filetext, srvrname = saveonserver(fileinfo)
        except:
            errmsg = '<h2>Error</h2><p>%s</p><p>%s</p>' % tuple(sys.exc_info()[:2])
            print(html % errmsg)
        else:
            print(goodhtml % (cgi.escape(fileinfo.filename),
                              cgi.escape(srvrname),
                              cgi.escape(filetext)))
main()






























