print("My name is Mohammed Mudabir Raza")
#This is  single
"""
This is a 
double line 
comment syntax

""" 
IntVal=10
boolVal=True
charVal='A'
floatVal=1.2
doubleVal=131.2334590
print("Data type is:", type(IntVal))
print("Data type is:", type(boolVal))
print("Data type is:", type(charVal))
print("Data type is:", type(floatVal))
print("Data type is:", type(doubleVal))
globalVar="This is global"
def f():
 localVar="This is local"
 print(localVar)
print(globalVar)
f()
def s():
 global var1
 var1="this is a global online"
s()
print(var1)