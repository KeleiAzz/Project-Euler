__author__ = 'keleigong'
total = 0
a = 3
b = 5
m3 = []
while a <1000:
    total+=a
    m3.append(a)
    a+=3

while b<1000:
    if not b in m3:
        total+=b
    b+=5

print total
