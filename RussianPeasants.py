import math
import csv

def divide(a):
    print(a)
    bigcount = 0
    count = 0
    while a > 1:
        bigcount += 1
        if a%2 != 0:
            count += 1
        a = a/2
        a = int(a)
        if a == 1:
            count += 1
    print("divides "+str(bigcount)+" times and gives "+str(count)+" number(s) to be added.")

def divisions():
    results = {}
    for i in range(2, 100):
        bigcount = 0
        count = 0
        a = i
        while a > 1:
            bigcount += 1
            if a%2 != 0:
                count += 1
            a = a/2
            a = int(a)
            if a == 1:
                count += 1
        results[i] = count
    return results

