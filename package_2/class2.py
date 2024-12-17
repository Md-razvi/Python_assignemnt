class Class2:
    def __init__(self,age):
        self.age=age
        print("Class2 construcotr:Object of class1")
    def Display_Msg(self,message):
        print(message+str(self.age))