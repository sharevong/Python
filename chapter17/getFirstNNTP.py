#!/usr/bin/env python

import nntplib
import socket

HOST = 'your.nntp.server'
GRNM = 'comp.lang.python'
USER = 'wesley'
PASS = "you'llNeverGuess"

def main():
    try:
        n = nntplib.NNTP(HOST) # NNTP(HOST, user=USER, password=PASS)
    except socket.gaierror as e:
        print('ERROR: cannot reach %s, error: %s' % (HOST, e))
        return
    except nntplib.NNTPPermanentError as e:
        print('ERROR: access denied on %s, error: %s' % (HOST, e))
        return
    print('*** Connected to host %s' % HOST)

    try:
        rsp, ct, fst, lst, grp = n.group(GRNM)
    except nntplib.NNTPPermanentError as e:
        print('ERROR: cannot load group %s, error: %s' % (GRNM, e))
        print('Server may require authentication')
        print('Uncomment/edit login line above')
        n.quit()
        return
    except nntplib.NNTPReplyError as e:
        print('ERROR: group %s unavailable, error: %s' % (GRNM, e))
        n.quit()
        return
    print('*** Found newsgroup %s' % GRNM)

    rng = '%s-%s' % (lst, lst)
    rsp, frm = n.xhdr('from' ,rng)
    rsp, sub = n.xhdr('subject', rng)
    rsp, dat = n.xhdr('date', rng)
    print('''*** Found last article(#%s):
    From: %s
    Subject: %s
    Date: %s''' % (lst, frm[0][1], sub[0][1], dat[0][1]))

    rsp, anum, mid, data = n.body(lst)
    displayFirst20(data)
    n.quit()

def displayFirst20(data):
    print('*** First (<=20) meaningful lines:\n')
    count = 0
    lines = (line.rstrip() for line in data)
    lastBlank = True
    for line in lines:
        if line:
            lower = line.lower()
            if (lower.startswith('>') and not \
                lower.startswith('>>>')) or \
                lower.startswith('|') or \
                lower.startswith('in article') or \
                lower.endswith('writes:') or \
                lower.endswith('wrote:'):
                continue
            if not lastBlank or (lastBlank and line):
                print('%s' % line)
            if line:
                count += 1
                lastBlank = False
            else:
                lastBlank = True
            if count == 20:
                break

if __name__ == '__main__':
    main()


