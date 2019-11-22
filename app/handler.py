#!/usr/bin/env python

#import glob
import sys
sys.path.append('gen-py')
#sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from serv import Remote
#from tutorial.ttypes import InvalidOperation, Operation

#from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class Handler:
    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def add(self, n1, n2):
        print('add(%d,%d)' % (n1, n2))
        return n1 + n2

    def zip(self):
        print('zip()')


if __name__ == '__main__':
    handler = Handler()
    processor = Remote.Processor(handler)
    transport = TSocket.TServerSocket(host="0.0.0.0", port=9090)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    #server = TServer.TThreadedServer(
    #        processor, transport, tfactory, pfactory)
    server = TServer.TThreadPoolServer(
            processor, transport, tfactory, pfactory)

    print('Starting the server...')
    server.serve()
    print('done.')
