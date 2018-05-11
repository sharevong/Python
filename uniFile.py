#!/usr/bin/env python

'''
an example of reading and writing Unicode strings:
write a Unicode string to file in utf-8 and read it back in
'''

CODEC = 'utf-8'
FILE = 'unicode.txt'

hello_out = u"Hello world\n"
bytes_out = hello_out.encode( CODEC )
f = open( FILE, 'w' )
f.write( bytes_out )
f.close()

f = open( FILE, 'r' )
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode( CODEC )
print hello_in,
