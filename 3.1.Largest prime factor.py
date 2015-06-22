import math
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
    

    