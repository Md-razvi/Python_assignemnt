# Create a sub class and try to access the private fields and methods from sub class.
class PrivateClassField:
    _var="This is a protected variable"
    var="This is public variable"
    def __init__(self,name):
        self.__name=name # private field 
    def __method(self):
        print("This is a private method") # private method
    def getName(self):
        return self.__name
    def accessPrivatemethod(self): #public method
        self.__method() #accessing private method using public method
        
class SubClass(PrivateClassField):
    def __init__(self,name):
        super().__init__(name)
    
        
obj=SubClass("John")
# Accessing name a private class
print(obj.getName()) # private field cannot be accessed but can be technically inherited
print(obj._var) # Accessing 
print(obj.var)
obj.accessPrivatemethod()

    


        
