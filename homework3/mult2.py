#!/usr/bin/python2
# ECE 2524 Homework 3 Problem 1 <Xingjian Ma>
import sys
import argparse
import fileinput
from sys import argv
parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(description='Process some numbers.')
parser.add_argument("files",nargs = '*' )
parser.add_argument("--ignore-blank","--ignore_blank", help = "cause the program to simply ignore blank lines in the input", action = "store_true")
parser.add_argument("--ignore-non-numeric","--ignore_non_numeric", help = "cause the program to ignore lines that do not contain numeric input", action = "store_true")
args = parser.parse_args()
total = 1
if not args.files:
    line = sys.stdin.readline()
    while line:
        if line == '\n':
            if not args.ignore_blank:
                print >> sys.stdout, total
                total = 1
        else:
            try:
                total = total*float(line)
            except ValueError as e:
                if not args.ignore_non_numeric:
                    print >> sys.stderr, e
                    sys.exit(1)
        line = sys.stdin.readline()
    print >> sys.stdout, total
else:
    for line in fileinput.input(args.files):
        if line == '\n':
            if not args.ignore_blank:
                print >> sys.stdout, total
                total = 1
        else:
            try:
                total = total*float(line)
            except ValueError as e:
                if not args.ignore_non_numeric:
                    print >> sys.stderr, e
                    sys.exit(1)
    print >> sys.stdout, total

