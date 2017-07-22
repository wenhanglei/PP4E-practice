"""
XML parsing: DOM gives whole document to the application as a traversable object
"""

import pprint
import xml.dom.minidom
from xm.dom.minidom import Node

doc = xml.dom.minidom.parse("books.xml")

mapping = {}
for node in doc.getElementsByTagName("book"):
    isbn = node.getAttridute("isbn")
    L = node.getElementsByTagName("title")
    for node2 in L:
        title = ""
        for node3 in node2.childNodes:
            if node3.nodeType == Node.TEXT_NODE:
                title += node3.data
        mapping[isbn] = title

pprint.pprint(mapping)





























