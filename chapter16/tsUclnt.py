#!/usr/bin/env python

from socket import *


HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('> ')
    if not data:
        break
    udpCliSock.sendto(bytes(data, encoding='utf8'), ADDR)
    data, addr = udpCliSock.recvfrom(BUFSIZ)
    if not data:
        break
    print(data)

udpCliSock.close()