#1. Write a class with a default constructor, one argument constructor and two argument 
# constructors. Instantiate the class to call all the constructors 
# of that class from a main class

# Sol1
#A constructor in Python cannot be run multiple times automatically for the same object.
# It is invoked only once when the object is instantiated.
class DefaultConstructor:
    def __init__(self):
        print("This is a default constructor")
class ConstructorWith1Args:
    def __init__(self,name):
        self.name=name
    def func1(self):
        print(f"My name is {self.name}")
class ConstructorWith2Args:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func1(self):
        print(f"My name is {self.name} and my age is {self.age}")

a=DefaultConstructor()
b=ConstructorWith1Args("Sasuke")
b.func1()
c=ConstructorWith2Args("Hinata Hyuga",32)
c.func1()
#2. Call the constructors(both default and 
# argument constructors) of super class from a child class
class ChildClass(ConstructorWith2Args):
    def __init__(self,name,age):
        super().__init__(name,age)
    def funct(self):
        print("I am {0} son of Hinata of age {1}".format(self.name,self.age))
d=ChildClass("Boruto",10)
d.funct()
# Apply private, public, protected and default access modifiers to the constructor
class AccessModifiers:
    #public accessifier
    name=None
    #protected accessifier
    _age=None
    #private accessifier
    __proffession=None
    def __init__(self,name,age,proffession):
        self.name=name
        self._age=age
        self.__proffession=proffession
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self._age)
    def getProffession(self):
        print(self.__proffession)
f=AccessModifiers("Naruto",34,"hokage")
f.getName()
f.getAge()
f.getProffession()
    
        
    