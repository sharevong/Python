#!/usr/bin/env python

from socketserver import TCPServer as TCP, StreamRequestHandler as SRH
from time import ctime


HOST = 'localhost'
PORT = 21567
ADDR = (HOST, PORT)
BUFSIZ = 1024

class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from:', self.client_address)
        msg = '[%s] %s' % (ctime(), self.request.recv(BUFSIZ))
        self.request.send(bytes(msg, encoding='utf8'))

tcpServer = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServer.serve_forever()
