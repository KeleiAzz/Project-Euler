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
k=3
total =2
while k<2000000:
    if is_prime(k):
        total += k
    k+=2
    
print total