for i in range(333,500,1):
    for j in range(i):
        if i*i == j*j + (1000-i-j)**2:
            print 'a='+str(j)+',b='+str(1000-i-j)+',c='+str(i)
            break