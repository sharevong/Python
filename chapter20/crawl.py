#!/usr/bin/env python

from sys import argv
from os import makedirs, unlink, sep
from os.path import dirname, exists, isdir, splitext
from html.parser import HTMLParser
from urllib.request import urlretrieve, urlparse, urljoin
from formatter import DumbWriter, AbstractFormatter
from io import StringIO


class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.anchorlist = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a' or tag == 'A':
            for t in attrs:
                if t[0] == 'href' or t[0] == 'HREF':
                    self.anchorlist.append(t[1])


class Retriever(object):
    def __init__(self, url):
        self.url = url
        self.file = self.filename(url)

    def filename(self, url, deffile='index.html'):
        parsedurl = urlparse(url, 'http:', 0)
        path = parsedurl[1] + parsedurl[2]
        ext = splitext(path)
        if ext[1] == '':
            if path[-1] == '/':
                path += deffile
            else:
                path += '/' + deffile
        ldir = dirname(path)
        if sep != '/':
            ldir = ldir.replace('/', sep)
        if not isdir(ldir):
            if exists(ldir):
                unlink(ldir)
            makedirs(ldir)
        return path

    def download(self):
        try:
            retval = urlretrieve(self.url, self.file)
        except IOError:
            retval = '*** Error: invalid URL %s' % self.url
        return  retval

    def parseAndGetLinks(self):
        self.parser = MyHTMLParser()
        # AbstractFormatter(DumbWriter(file=StringIO()))
        self.parser.feed(open(self.file).read())
        self.parser.close()
        return self.parser.anchorlist


class Crawler(object):
    count = 0
    def __init__(self, url):
        self.q = [url]
        self.seen = []
        self.dom = urlparse(url)[1]

    def getPage(self, url):
        r = Retriever(url)
        retval = r.download()
        if retval[0] == '*':
            print(retval, '... skipping parse')
            return
        Crawler.count += 1
        print('\n(', Crawler.count, ')')
        print('URL:', url)
        print('FILE:', retval[0])
        self.seen.append(url)

        links = r.parseAndGetLinks()
        for eachLink in links:
            if eachLink[:4] != 'http' and eachLink.find('://') == -1:
                eachLink = urljoin(url, eachLink)
            print('*', eachLink)
            link = eachLink.lower()
            if link.find('mailto:') != -1:
                print('... discarded, mailto link')
                continue

            if eachLink not in self.seen:
                if eachLink.find(self.dom) == -1:
                    print('... discarded, not in domain')
                else:
                    if eachLink not in self.q:
                        self.q.append(eachLink)
                        print('... new, added to q')
                    else:
                        print('... discarded, already in q')
            else:
                print('... discarded, already processed')

    def go(self):
        while self.q:
            url = self.q.pop()
            self.getPage(url)

def main():
    if len(argv) > 1:
        url = argv[1]
    else:
        try:
            url = input('Enter starting url: ')
        except (KeyboardInterrupt, EOFError):
            url = ''

    if not url:
        return
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()
