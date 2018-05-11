#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep

# get file name
while True:
    print "Enter file name"
    fname = raw_input( '>' )
    if os.path.exists( fname ):
        print "Error: '%s' already exists" % fname
    else:
        break

# get file content
all = []
print "Enter lines (. by itself to quit)"

# loop until enter .
while True:
    entry = raw_input( '>' )
    if entry == '.':
        break
    else:
        all.append( entry )

# write lines to file
fobj = open( fname, 'w' )
fobj.writelines( ['%s%s' % (x,ls) for x in all] )
fobj.close()
print 'DONE'
