#2-1
n = input()
s = int(n)
if s>10:
    print('big')
else:
    print('small')
    
if s%2 == 0:
    print('偶数')
else:
    print('奇数')
    
#2-2
for item in range(0,101):   
    print(item)

for item in range(100,-1,-1):
    print(item)
     
for item in range(100,-1,-2):
    print(item)
 
#2-3
while True:
    n = input()
    if n == 'hello':
        break

i = 100
while i >= 0:
    print(i)
    i = i-1

#2-4
for i in range(0,101):
    if i%2 == 0:
        print(i)

for i in range(1,10):
    for j in range(0,10):
        print(i,"*",j,"=",i*j)
     
        