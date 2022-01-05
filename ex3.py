#3-1
print(1024//3)
print(12**3)

#3-2
a = input()
b = input()

if int(a) < int(b):
    print('small')
elif int(a) > int(b):
    print('big')
else:
    print('equal') 
       
while True:
    n = input()
    if int(n)%5 == 0:
        break

a = input()
b = input()

if (int(a)*int(b))%2 == 0:
    print('odd')
else:
    print('even')
    
#3-3
a = input()
b = int(a)

if b>=50 and b<=100:
    print('True')
    
#入力は省略
if b%2 == 0 or b%5 == 0:
    print('ture')
    
#100までの素数
for item in range(0,101):
    if item != 1:
        if item%2 != 0 or item == 2:
            if item%3 != 0 or item == 3:
                if item%5 != 0 or item == 5:
                    if item%7 != 0 or item == 7:
                        print(item)

#おりんぴっく
y = input()
year = int(y)
if year%4 == 0:
    print('summer')
elif year%2 == 0:
    print('winter')
else:
    print('none')
    
    
                    
                
            
        
     
    
    
        