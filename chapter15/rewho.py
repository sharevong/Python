#!/usr/bin/env python

from os import popen
from re import split


f = popen('who', 'r')           # who can be replaced with dir on windows system
for eachLine in f.readlines():  # f.readlines() can be replaced with f
    print split('\s\s+|\t', eachLine)
f.close()
