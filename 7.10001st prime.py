import math


def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n%3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f+2) == 0:
                return False
            f = f+6
        return True

def find_prime2(n):
    lastFactor=[]
    if n%2 == 0:
        lastFactor.append(2)
        n = n/2
        while n%2 == 0:
            lastFactor.append(2)
            n = n/2
    else:
        lastFactor.append(1)
    
    factor = 3
    maxFactor = math.sqrt(n)
    while n>1 and factor <= maxFactor:
        if n % factor == 0:
            n = n/factor
            lastFactor.append(factor)
            while n%factor == 0:
                n = n/factor
                lastFactor.append(factor)
            maxFactor = math.sqrt(n)
            
        factor =factor + 2
    
    if n == 1:
        return lastFactor
    else:
        lastFactor = lastFactor+[n]
        return lastFactor[1:]
count =1
p=3

while count<10001:
    #print p
    if len(find_prime2(p)) == 1:
        count += 1
        #print count
        if count == 10001:
            print p
    p+=2