# ECE 2524 Homework 2 Problem 1 <Xingjian Ma>
from sys import argv
filename = argv[1]
f = open(filename, 'r')
for line in f:
    print "%s\t%s" %(line.split(':')[0], line.split(':')[6]),
