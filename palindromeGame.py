def reverse(a):
    return int(str(a)[::-1])

def isPalindrome(a):
    if str(a)[::-1] == str(a):
        return True
    else:
        return False

count = 0
def playGame(a, count=-1):
    count += 1
    if count == 0:
        print(str(a))
    if isPalindrome(a) == True:
        count = str(count)
        result = " is a "+count+" step palindrome"
        result += " ending at "+str(a)
        print(result)
    else:
        playGame(a+reverse(a), count)
        
