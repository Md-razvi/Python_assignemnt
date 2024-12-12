#1. Write a program to print “Bright IT Career” ten times using for loop
import math
for i in range(10):
    print(str(i+1)+". Bright IT Career")
#2. Write a java program to print 1 to 20 numbers using the while loop.
i=1
while i<=20:
    print(i,end=" ")
    i+=1
print(" ")
#3. Program to equal operator and not equal operators
a=10
b=12
print(a==b)
print(a!=b)
#4. Write a program to print the odd and even numbers.
odd=""
even=""
for i in range(20):
    if (i+1)%2==0:
        even=even+str(i+1)+" "
    else:
        odd=odd+str(i+1)+" "
print("The even numbers",even)
print("The odd numbers",odd)
#5. Write a program to print largest number among three numbers.
f=12
g=34
h=90
print(" ")
if f>g:
    if(f>h):
        print("f is greater")
    else:
        print("h is greater")
else:
    if(g>h):
        print("g is greater")
    else:
        print("h is greater")

#6. Write a program to print even number between 10 and 20 using while
k=11
while k<20:
    if k%2==0:
        print(k,end=" ")
    k+=1
print(" ")
#7. Write a program to print 1 to 10 using the do-while loop statement.
#   There is no do-while loop in python
#8. Write a program to find Armstrong number or not

def Armstrong(x):
    sum=0
    power=0
    actualnum=x
    powernum=x
    isTrue=False
    while(powernum!=0):
        power+=1
        powernum//=10
    while(x!=0):
        rem=x%10
        sum=sum+rem**power
        x//=10
    if(actualnum==sum):
        isTrue=True    
        return isTrue
    return isTrue
    
y=Armstrong(371)
print("The given number is armstrong:",y)

#9. Write a program to find the prime or not.
def Prime(x):
    isPrime=True
    if x<=2:
        return isPrime
    if x>2:
        y=math.isqrt(x)
        for i in range(2,y+1):
            if(x%i==0):
                isPrime=False
                break
            
    return isPrime

z=Prime(2)
print('Is it prime:',z)

#10. Write a program to palindrome or not.
def isPalindorme(x):
    actualnum=x
    sum=0
    tenth_place=0
    while(x>0):
        rem=x%10
        sum=sum*10+rem
        x//=10
    if sum==actualnum:
        return True
    else:
        return False
isPal=isPalindorme(13221)
print("Is it palindrome",isPal)        
#11. Program to check whether a number is EVEN or ODD using switch
num=12

match (num%2):
    case 0:
        print("The number is even")
    case 1:
        print("The number is odd")
    case default:
        print("Please enter a number")
#12 Print gender (Male/Female) program according to given M/F using switch
gender='M'
match(gender):
    case 'M':
        print("He is a male")
    case 'F':
        print("She is a female")
    case default:
        print("Please enter correct gender")
    
 