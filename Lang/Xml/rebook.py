"""
XML parsing: regular expressions (no robust or general)
"""
import re, pprint
text = open('books.xml').read()
pattern = '(?s)isbn="(.*?)".*?<title>(.*?)</title>'
found = re.findall(pattern, text)
mapping = {isbn: title for (isbn, title) in found}
pprint.pprint(mapping)















