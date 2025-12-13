import math

def check(n):
    if n%9 == 0:
        for i in str(n):
            if i in ('0','1','2','3','5','7','8','9'):
                return False
        return True
    return False

def checkit(n):
    list = []
    for i in range(666,n):
        if check(i) == True:
            list.append(i)
    print(list)
