#!/usr/bin/env python

import threading
from time import sleep, ctime

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        print('starting ', self.name, ' at: ', ctime())
        self.res = self.func(*self.args)
        print(self.name, ' finished at: ', ctime())\

    def getResult(self):
        return self.res