import random
while True:
    com = random.randint(1,3)
    npc = '' 
    if com == 1:
        npc = "gu"
    elif com == 2:
        npc = 'choki'
    else:
        npc = 'pa'
        
    you = input()    
    
    if you == 'fin':
        break
    
    print('npc is',npc)
    
    if you == "gu" and npc == 'choki':
        print('you win')
        break
    elif you == "gu" and npc == 'pa':
        print('you lose')
        break   
    elif you == "choki" and npc == 'pa':
        print('you win')
        break
    elif you == "choki" and npc == 'gu':
        print('you lose')
        break      
    elif you == "pa" and npc == 'gu':
        print('you win')
        break
    elif you == "pa" and npc == 'choki':
        print('you lose')
        break
    else:
        print('drow')
    