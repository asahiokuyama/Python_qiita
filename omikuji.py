#import
import tkinter as tk
import random 

def dsiplabel():
    kuji = ['大吉','中吉','小吉','凶']
    
    #ラベルの文字を修正する
    lbl.configure(text=random.choice(kuji))

root = tk.Tk()#画面をつくRU

root.geometry("800x400")#画面の大きさ設定

lbl = tk.Label(text='LABEL')#ラベル作成
btn = tk.Button(text='PUSH',command=dsiplabel)#ボタン作成。関数の紐づけ

lbl.pack()#ラベル配置
btn.pack()#ボタン配置

tk.mainloop()#ウィンドウ表示