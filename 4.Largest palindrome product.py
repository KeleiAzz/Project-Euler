def ispalindrome(x):
    digit=[]
    t = 1
    while t<x:
        digit.append(x/t%10)
        t*=10
    temp=digit[::-1]
    #print digit
    #print temp
    
    if temp == digit:
        return True
    else:
        return False
result=[]
for i in range(100,1000,1):
    for j in range(100,1000,1):
        if ispalindrome(i*j):
            result.append(i*j)
            