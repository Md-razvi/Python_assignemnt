# Create three methods in each class, 
# 2 methods are specific to each class and third method (override method) 
# should be in all three Classes A, B and C
# Call an overridden method with super class reference to B and C class’s objects
class A:
    def A_Method1(self):
        print("This is a A_method1")
    def A_Method2(self): 
        print("This is a A_method2")
    def A_Method3(self):
        print("This is a A_method3")
class B(A):
    def B_Method1(self):
        print("This is a B method1")
    def B_Method2(self): 
        print("This is a B method2")
    def A_Method3(self):
        print("This is a A_method in B")
class C(B):
    def C_Method1(self):
        print("This is a C method1")
    def C_Method2(self):
        print("This is a C method2")
    def A_Method3(self):
        print("This is a A_method in C")
obj1=A()
obj1.A_Method1()
obj1.A_Method2()
obj1.A_Method3()
obj2=B()
obj2.B_Method1()
obj2.B_Method2()
obj2.A_Method3()
obj3=C()
obj3.C_Method1()
obj3.C_Method2()
obj3.A_Method3()