#!/usr/bin/env python

import _thread
from time import sleep, ctime

def loop0():
    print('start loop0 at: ', ctime())
    sleep(4)
    print('loop0 done at: ', ctime())

def loop1():
    print('start loop1 at: ', ctime())
    sleep(2)
    print('loop1 done at: ', ctime())

def main():
    print('starting at: ', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)        # wait loop0 loop1 stop with sleep
    print('all done at: ', ctime())

if __name__ == '__main__':
    main()
