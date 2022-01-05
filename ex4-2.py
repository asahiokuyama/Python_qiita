class Human:
    def __init__(self,name,year):
        self.myname = name
        self.myyear = year
    def hello(self):
        print("myname is " + self.myname)
    def run(self):#追加
        print(self.myname + " is running")#追加
    def old(self):
        print(self.myyear)

John = Human('John',18)
John.hello()
John.run()#追加

Bob = Human('Bob',20)
Bob.hello()
Bob.old()