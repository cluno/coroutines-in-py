import xml.sax

def load(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

coroutine = load('coroutine', '../part1/coroutine.py')
from coroutine import coroutine

class EventHandler(xml.sax.ContentHandler):
    def __init__(self, target):
        self.target = target
    def startElement(self,name,attrs):
        self.target.send(('start', (name,attrs._attrs)))
    def characters(self,text):
        self.target.send(('text',text))
    def endElement(self,name):
        self.target.send(('end', name))

if __name__ == '__main__':
    from coroutine import *

    @coroutine
    def printer():
        while True:
            event = (yield)
            print event

    xml.sax.parse("allroutes.xml", EventHandler(printer()))