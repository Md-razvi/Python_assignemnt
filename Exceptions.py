# Write a program to generate Arithmetic Exception without exception handling
# Handle the Arithmetic exception using try-catch block
# Write a program to generate Arithmetic Exception
# Write a program with finally block
def divide_numbers(a, b):
    result = a / b  
    return result
try:
    a=divide_numbers(10, 0)
    print(a)
except ZeroDivisionError as e:
    print (f'This is a exception: {e}')
finally:
    print("This is a final block")

# Write a method which throws exception, Call that method in main class without try block
# Write a program to throw exception with your own message
def ArithematicExceptionMethod(a,b):
    if b==0:
        raise ZeroDivisionError("Yo bro division cannot  by zero cannot done")
    else:
        return a/b
#ArithematicExceptionMethod(12,0)
# Write a program with multiple catch blocks
def example_multiple_exceptions(a, b, index):
    try:
        result = a / b
        print(f"Division Result: {result}")
        sample_list = [10, 20, 30]
        print(f"Accessing List Element: {sample_list[index]}")
    except ZeroDivisionError:
        print("Error: You attempted to divide by zero.")
    except IndexError:
        print("Error: List index is out of range.")
    except Exception as e:
        print(f"General Exception Caught: {e}")
example_multiple_exceptions(12,12,4)   


# Write a program to create your own exception
class MyOwnException(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(self.message)
def Check_positive_number(r):
    if r<0:
        raise MyOwnException("Error: This is a negative number")
    else:
        print(f"Indeed it isa valid number {r}")
# Check_positive_number(-12)
# Write a program to generate FileNotFoundException
def FileNotFoundException():
    try:
        with open("file1.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print(f"FileNotFoundError Caught: {e}")
FileNotFoundException()
# Write a program to generate ClassNotFoundException
def Class_Not_Found():
    try:
        from math import MyClass  # Assuming my_module is in the same directory
    except ImportError as e:
        print(f"ImportError: {e}") 
Class_Not_Found()
# Write a program to generate IOException
def Io_exception():
    try:
        with open("non_existent_file.txt", "r") as file: 
            file.read() 
    except IOError as e:
        print(f"An IOError occurred: {e}")
Io_exception()
# Write a program to generate NoSuchFieldException
class MyClass1:
    def __init__(self, value):
        self.my_value = value

def FieldException():
    try:  
        obj = MyClass1(10)
        nonExistentAttribute = obj.existentField 
    except AttributeError as e:
        print(f"AttributeError: {e}")

FieldException()
 