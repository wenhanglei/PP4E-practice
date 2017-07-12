"""
###################################################################################
Display any CGI (or other) server-side file without running it. The filename can
be passed in a URL param or form field (use "localhost" as the server if local):

Users can cut-and-paste or "View Source" to save file loacally. On IE, runnin the
text/plain version (formatted=False) sometimes pops up Notepad, but end-lines are 
not always in DOS format; Netscape shows the text correctly in the browser page
instead. Sending the file in text/HTML mode works on both browsers--text is 
displayed in the browser response page correctly. We also check the filename here
to try to avoid showing private files; this may or may not prevent access to such
files in general: don't install this script if you can't otherwise secure source?
##################################################################################
"""

import cgi, os, sys
formatted = True
privates = ['PyMailCgi/cgi-bin/secret.py']

try:
    samefile = os.path.samefile
except:
    def samefile(path1, path2):
        apath1 = os.path.abspath(path1).lower()
        apath2 = os.path.abspath(path2).lower()
        return apath1 == apath2

html = """
<html><title>Getfile response</title>
<h1>Source code for: '%s'</h1>
<hr>
<pre>%s</pre>
<hr></html>
"""

def restricted(filename):
    for path in privates:
        if samefile(path, filename):
            return True

try:
    form = cgi.FieldStorage()
    filename = form['filename'].value
except:
    filename = 'cgi-bin/getfile.py'

try:
    assert not restricted(filename)
    filetext = open(filename).read()
except AssertionError:
    filetext = open(filename).read()
except AssertionError:
    filetext = '(File access denied)'
except:
    filetext = '(Error opening file: %s)' % sys.exc_info()[1]

if not formatted:
    print('Content-type: text/plain\n')
    print(html % (filename, cgi.escape(filetext)))






























