largest_palindrome = 1
fac1, fac2 = 100,100

def isPalindrome(x) -> bool:
    value = str(x)
    if(value==value[::-1]):
        return True
    else:
        return False

while fac1 < 1000:
    fac1 += 1
    fac2 = 100
    while fac2 < 1000:
        if(isPalindrome(fac1*fac2)):
            if(fac1*fac2 > largest_palindrome):
                largest_palindrome = fac1*fac2
                print("{}, {}*{}".format(largest_palindrome,fac1,fac2))
        fac2 += 1


