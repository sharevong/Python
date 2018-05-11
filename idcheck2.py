#!/usr/bin/env python

import string

alphas = string.letters + "_"
nums = string.digits
keywords = ( 'and', 'as', 'assert', 'break', 'class', 'continue',
             'def', 'del', 'elif', 'else', 'except', 'exec', 
             'finally', 'for', 'from', 'global', 'if', 'import',
             'in', 'is', 'lambda', 'not', 'or', 'pass', 'print',
             'raise', 'return', 'try', 'while', 'with', 'yield',
             'None' )

print 'Welcome to the Identifier Checker v2.0'

myInput = raw_input( "Identifier to test? " )
if len(myInput) == 0:    # check input empty
    print 'Invalid: no input'
else:
    if myInput[0] not in alphas:   # check first symbol alphabetic
        print 'Invalid: first symbol must be alphabetic'
    elif myInput in keywords:  # check keyword
        print 'Invalid: identifier must not be keyword'
    else:
        for char in myInput:  # check character in input
            if char not in alphas + nums:
                print 'Invalid: remain symbols must be alphanumeric'
                break
        else:
            print 'okay as an identifier'
