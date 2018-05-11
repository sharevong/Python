#!/usr/bin/env python

'readTextFile.py -- read and display text file'

# get file name
fname = raw_input( 'Enter filename: ' )
print

# open file to read
try:
    fobj = open( fname, 'r' )
except IOError, e:
    print "*** file open error: ", e
else:
    # display content
    for line in fobj:
        print line,
    fobj.close()
