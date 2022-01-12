import tkinter as tk
import random

def janken(num):
    com = random.randint(1,3)

    if com == 1:
        comlbl.config(text='cpの手:グー')
        
        if num == 2:
            result.config(text='あなたのまけ')
        elif num == 3:
            result.config(text='あなたのかち')
            
    elif com == 2:
        comlbl.config(text='cpの手:チョキ')
        
        if num == 1:
            result.config(text='あなたのかち')
        elif num == 3:
            result.config(text='あなたのまけ')
        
    elif com == 3:
        comlbl.config(text='cpの手:パー')
        
        if num == 1:
            result.config(text='あなたのまけ')
        elif num == 2:
            result.config(text='あなたのかち')
    
    if num == com:
        result.configure(text='あいこ')
        
    

root = tk.Tk()
root.geometry("500x500")

lbl = tk.Label(text='じゃんけんゲーム')
comlbl = tk.Label(text='0')
result = tk.Label(text='?')

btn = tk.Button(text='グー',command=lambda: janken(1))
btn2 = tk.Button(text='チョキ',command=lambda: janken(2)) 
btn3 = tk.Button(text='パー',command=lambda: janken(3))

lbl.pack(fill='x',pady=100)

btn.pack(fill='x',padx=30,side='top')
btn2.pack(fill='x',padx=30,side='top')
btn3.pack(fill='x',padx=30,side='top')

comlbl.pack(fill='x',pady=30,side='top')
result.pack(fill='x',pady=30,side='top')

tk.mainloop()