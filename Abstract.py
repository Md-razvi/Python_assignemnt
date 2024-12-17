#1. Create an abstract class with abstract and non-abstract methods.
#2. Create a sub class for an abstract class. Create an object in the child class for the
# abstract class and access the non-abstract methods
#3. Create an instance for the child class in child class and call abstract methods
#4. Create an instance for the child class in child class and call non-abstract methods
from abc import ABC,abstractmethod
class AbstractClass(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def AbstractMethod(self):
        pass
    def Non_abstractMethod(self):
        print("This is a non abstract method")
class ChildClass(AbstractClass):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def AbstractMethod(self):
        print("This is an abstract method")     

a=ChildClass("Puspha",56)
a.AbstractMethod()
a.Non_abstractMethod()