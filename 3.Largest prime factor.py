x=600851475143

def find_prime(x):
    p=[2]
    while x!=1 and x!=0:
        #print 'x=' + str(x)
        i=p[-1]
        #print 'i='+str(i)
        while i<=x:
            if x%i == 0:
                p.append(i)
                #print i
                x/=p[-1]
                i+=x
    
                #break
            i+=1
    return p[1:]

print find_prime(x)