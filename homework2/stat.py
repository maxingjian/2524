# ECE 2524 Homework 2 Problem 3 <Xingjian Ma>
from sys import argv
filename = argv[1]
f = open(filename, 'r')
print "ACCOUNT SUMMARY"
first_line = f.readline()
Total = Min = Max = float(first_line.split()[2])
Min_name = Max_name = first_line.split()[1]
Count = 1
for line in f:
    Count = Count + 1
    Total = Total + float(line.split()[2])
    if float(line.split()[2]) < Min:
        Min = float(line.split()[2])
        Min_name = line.split()[1]
    if float(line.split()[2]) > Max:
        Max = float(line.split()[2])
        Max_name = line.split()[1]
print "Total amount owed = %.2f" %Total
# In order to print the average amount as exactly same
# as 23.30 in the sample output, the result is rounded
# to 1 digit after the decimal point then followed by
# a '0', since the actual result would be 23.26
print "Average amount owed = %.1f0" % (Total/Count)
print "Maximum amount owed = %.2f by %s" %(Max, Max_name)
print "Minimum amount owed = %.2f by %s" %(Min, Min_name)
