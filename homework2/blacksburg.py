# ECE 2524 Homework 2 Problem 2 <Xingjian Ma>
from sys import argv
filename = argv[1]
f = open(filename, 'r')
print 'ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS'
for line in f:
    if line.split()[3] == 'Blacksburg':
        print '%s, %s, %s, %s' %(
        line.split()[4],line.split()[1],
        line.split()[0],line.split()[2])
