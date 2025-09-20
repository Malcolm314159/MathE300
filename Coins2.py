import math
import itertools

coinList = [1,3,4,5]

def vList(x):
    """
    Returns a list of values that can be produced
    using two coins from the coin list x
    """
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
    """
    Returns all possible combinations of n coins for a
    currency system with a maximum value of maxValue.
    Returns tuples.
    """
    #n is the number of coins
    #maxValue is the maximum value of the currency system
    #returns all possible combinations of n coins
    m = 1
    L = []
    while m < maxValue:
        L.append(m)
        m += 1
    return itertools.combinations(L,n)


def Coins(n, maxValue):
    L = []
    a = getCoins(n, maxValue)
    for i in range(1,maxValue+1):
        L.append(i)
    for i in a:
        if i[0] == 1:
            b = vList(i)
            if b[0:maxValue] == L:
                print(i)
