def palindrome(str,a,b):

    if a>=b:
        return 1
    if str[a]!=str[b]:
        return 0
    return palindrome(str,a+1,b-1)

str=input()
print(palindrome(str,0,len(str)-1))