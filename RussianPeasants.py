import math
import csv

def divide(a):
    print(a)
    bigcount = 0
    count = 0
    while a > 1:
        bigcount += 1
        a = a/2
        if a%2 != 0:
            count += 1
        a = int(a)
    print("divides "+str(bigcount)+" times with "+str(count)+" odd quotients.")

def divisions():
    results = {}
    for i in range(2, 100):
        bigcount = 0
        count = 0
        a = i
        while a > 1:
            bigcount += 1
            a = a/2
            if a%2 != 0:
                count += 1
            a = int(a)
        results[i] = count
    return results

r = divisions()
