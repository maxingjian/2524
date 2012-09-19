#!/usr/bin/python2
# ECE 2524 Homework 3 Problem 1 <Xingjian Ma>
import sys
import argparse
parser = argparse.ArgumentParser(description='Process some numbers.')
args = parser.parse_args()
total = 1
line = sys.stdin.readline()
while line:
    if line == '\n':
        print >> sys.stdout, total
        total = 1
    else:
        try:
            total = total*float(line)
        except ValueError as e:
            print >> sys.stderr, e
            sys.exit(1)
    line = sys.stdin.readline()
print >> sys.stdout, total

