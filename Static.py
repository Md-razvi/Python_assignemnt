#1. Define a static variable and access that through a class
class Class1:
    staticValue='this is static value'
print(Class1.staticValue)
#2. Define a static variable and access that through a instance
#3. Define a static variable and change within the instance
#4. Define a static variable and change within the class
class Class2:
    staticValue2="This is a static value 2"
    def __init__(self,instance1):
        self.instance1=instance1 #instance value

obj1=Class2("this is object")
print(obj1.staticValue2)
obj1.staticValue2="Value is Changed using obj1"
print(obj1.staticValue2)
Class2.staticValue2="this is Changed using Class"
print(Class2.staticValue2)