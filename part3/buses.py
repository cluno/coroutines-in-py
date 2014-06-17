def load(name, fpath):
    import os, imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))

coroutine = load('coroutine', '../part1/coroutine.py')
from coroutine import coroutine

@coroutine
def buses_to_dicts(target):
    while True:
        event, value = (yield)
        # Look for the start of a <bus> element
        if event == 'start' and value[0] == 'bus':
            busdict = { }
            fragments = []
            # Capture text of inner elements in a dict
            while True:
                event, value = (yield)
                if event == 'start':   fragments = []
                elif event == 'text':  fragments.append(value)
                elif event == 'end':
                    if value != 'bus': 
                        busdict[value] = "".join(fragments)
                    else:
                        target.send(busdict)
                        break

@coroutine
def filter_on_field(fieldname, value, target):
    while True:
        #print 'waiting on filter_on_filed..'
        d = (yield)
        if d.get(fieldname) == value:
            target.send(d)

@coroutine
def bus_locations():
    while True:
        #print 'waiting on bus_location..'
        bus = (yield)
        print "%(route)s,%(id)s,\"%(direction)s\","\
                "%(latitude)s,%(longitude)s" % bus

if __name__ == '__main__':
    import xml.sax
    from cosax import EventHandler

    xml.sax.parse("allroutes.xml",
            EventHandler(
                buses_to_dicts(
                filter_on_field("route", "147", 
                filter_on_field("direction", "North Bound",
                bus_locations())))
            ))

