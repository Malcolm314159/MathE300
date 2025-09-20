import math
import itertools

coinList = [1,3,4,5]

def vList(x):
    #x is a list of coins
    #returns a list of values creatable with two coins
    valueList = []
    for i in x:
        valueList.append(i)
        for k in x:
            valueList.append(k)
            valueList.append(i+k)
    valueList.sort()
    newList = []
    for i in valueList:
        if newList.count(i) == 0:
            newList.append(i)
    return newList

def getCoins(n, maxValue):
    #n is the number of coins
    #maxValue is the maximum value of the currency system
    #returns all possible combinations of n coins
    m = 1
    L = []
    while m < maxValue:
        L.append(m)
        m += 1
    return itertools.combinations(L,n)

L = []
a = getCoins(4,10)
for i in a:
    if i[0] == 1:
        b = vList(i)
        if b[0:10] == [1,2,3,4,5,6,7,8,9,10]:
            print(i)

