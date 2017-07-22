"""
XML parsing: SAX is a callback-based API for intercepting parser events
"""

import xml.sax, xml.sax.handler, pprint

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False
        self.mapping = {}

    def startElement(self, name, attributes):
        if name == "book":
            self.buffer = ""
            self.isbn = attributes["isbn"]
        elif name == "title":
            self.inTitle = True

    def characters(self, data):
        if self.inTitle:
            self.buffer += data

    def endElement(self, name):
        if name == "title":
            self.inTitle = False
            self.mapping[self.isbn] = self.buffer

parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('books.xml')
pprint.pprint(handler.mapping)



























