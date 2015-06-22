'''
def fb(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fb(x-1)+fb(x-2)

x = 1
total = 0
while fb(x)<4000000:
    if fb(x)%2==0:
        total += fb(x)
    x+=1

print total
'''

fb = [1,2]
nextnum = 0
total = 2
while nextnum<4000000:
    nextnum = fb[-1]+fb[-2]
    fb.append(nextnum)
    if nextnum%2==0:
        total+=nextnum

print total
