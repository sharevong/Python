#!/usr/bin/env python

queue = []
def enQ():
    queue.append( raw_input( 'Enter a new string: ' ).strip() )
def deQ():
    if len(queue) == 0:
        print 'Cannot pop from an empty queue'
    else:
        print 'Removed [', `queue.pop(0)`, ']'
def viewQ():
    print queue

CMDS = { 'e': enQ, 'd': deQ, 'v': viewQ }
def showmenu():
    pr = """
    (E)nqueue
    (D)equeue
    (V)iew
    (Q)uit
    Enter choice: """
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            if choice not in 'edvq':
                print 'Invalid choice, try again'
            else:
                break
        if choice == 'q':
            break
        CMDS[choice]()

if __name__ == "__main__":
    showmenu()
