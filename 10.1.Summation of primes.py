#The sieve of Eratosthenes

from math import *
limit = 2000000

crosslimit =int(floor(sqrt(limit)))

sieve = limit*[False]

for n in range(4,limit,2):
    sieve[n] = True
    
for n in range(3,crosslimit,2):
    if not sieve[n]:
        for m in range(n*n,limit,2*n):
            sieve[m]=True

sump = 0

for n in range(2,limit):
    if not sieve[n]:
        sump += n
        
        
print sump