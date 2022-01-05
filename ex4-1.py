import math

#4-1
y = input()
a = int(y)
    
def olympic(year):  
    if year%4 == 0:
        return('summer')
    elif year%2 == 0:
        return('winter')
    else:
        return('none')

print(olympic(a))

a = input()
b = input()
x = int(a)
y = int(b)

def countup(c,d):
    e = c+d
    return e

print(countup(x,y))

#三角形
#入力省略
def triangle(i,j):
    s = i * j
    s = s/2
    return s
print(triangle(x,y))

#三平方
def pita(x,y):
    z = x*x + y*y
    z = math.sqrt(z)
    return z
print(pita(x,y))
