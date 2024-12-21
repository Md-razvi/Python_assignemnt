# 1.Write two methods with the same name but different number of parameters of same type and call 
# the methods
# 2.Write two methods with the same name but different number of parameters 
# of different data type and call the methods
# 3.Write two methods with the same name and same number of parameters of same type
class MethodsOverloading:
    def method_Overloading(self,*args):
        str1=""
        for i in args:
            str1=str1+str(i)+" "
        print(str1)
a=MethodsOverloading()
a.method_Overloading(10)
a.method_Overloading(10,20)
a.method_Overloading(10,10.0,"String")

        
        