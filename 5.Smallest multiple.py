k=[r for r in range(1,13,1)] #1~12
#k.append(2520)

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

def findsm(k):
    s=2520
    for i in range(10,k+1,1):
        for j in find_prime(i):
            if s%j == 0:
                s = s/j
        s=s*i
    return s
''' 
        while s !=0:
            left =[]
            for i in k:
                left.append(s%i)
                if s%i!=0:
                    break
            if sum(left)==0:
                return s
            s+=2'''



print findsm(20)