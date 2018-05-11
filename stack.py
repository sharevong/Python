#!/usr/bin/env python

stack = []
def pushit():
    stack.append( raw_input( '>Enter a new string: ' ).strip() )
def popit():
    if len(stack) == 0:
        print 'Cannot pop from an empty stack'
    else:
        print 'Removed [', `stack.pop()`, ']'
def viewstack():
    print stack

CMDS = { 'u': pushit, 'o': popit, 'v': viewstack }
def showmenu():
    pr = """
    p(U)sh
    p(O)p
    (V)iew
    (Q)uit
    Enter choice: """
    while True:
        while True:
            try:
                choice = raw_input(pr).strip()[0].lower()
            except (EOFError, KeyboardInterrupt, IndexError):
                choice = 'q'
            print 'You picked: [%s]' % choice
            if choice not in 'uovq':
                print 'Invalid choice, try again'
            else:
                break
        if choice == 'q':
            break
        CMDS[choice]()

if __name__ == '__main__':
    showmenu()
