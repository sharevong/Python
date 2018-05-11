#!/usr/bin/env python

import os

for tmpdir in ('/tmp', r'c:\temp'):
    if os.path.isdir(tmpdir):
        break
else:
    print 'no temp dir available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temp dir'
    print cwd

    print '*** creating example dir'
    os.mkdir('example')
    os.chdir('example')
    cwd = os.getcwd()
    print '*** new working dir'
    print cwd

    print '*** original dir list: '
    print os.listdir(cwd)

    print '*** creating test file'
    fobj = open('test', 'w')
    fobj.write('foo\n')
    fobj.write('bar\n')
    fobj.close()

    print '*** update dir list: '
    print os.listdir(cwd)

    print '*** rename test to filetest.txt'
    os.rename( 'test', 'filetest.txt' )

    print '*** update dir list: '
    print os.listdir(cwd)

    path = os.path.join( cwd, os.listdir(cwd)[0] )
    print '*** full file pathname'
    print path

    print '*** pathname, basename =='
    print os.path.split(path)

    print '*** filename, extension =='
    print os.path.splitext( os.path.basename(path) )

    print '*** display file contents: '
    fobj = open( path )
    for line in fobj:
        print line,
    fobj.close()

    print '*** delete test file'
    os.remove(path)

    print '*** update dir list'
    print os.listdir(cwd)

    os.chdir(os.pardir)
    print '*** delete test dir'
    os.rmdir('example')

    print '*** DONE'
