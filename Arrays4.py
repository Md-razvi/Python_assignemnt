#1. Write a function to add integer values of an array
def Append(x,y):
    x.append(y)
    return x
list1=[1,2,3,4,5,6]
print(list1)
list2=Append(list1,7)
print(list2)
#2. Write a function to calculate the average value of an array of integers
list3=[10,12,23,24,55,67]
print(list3)
def Sum(x):
    sum=0
    length=len(x)
    for i in range(length):
        sum+=x[i]
    return sum
a=Sum(list3)
print(" ")
print("The sum of list3 is",a)        
#3. Write a program to find the index of an array element
def ArrIndex(x,y):
    arrlength=len(x)
    for i in range(arrlength):
        if(x[i]==y):
            return i
    return -1
index=ArrIndex(list3,67)
print("The index of value of 67 in list3 is",index)
#4. Write a function to test if array contains a specific value 
def isThereElement(x,y):
    isPresent=False
    arrlength=len(x)
    for i in range(arrlength):
        if(x[i]==y):
            isPresent=True
            break
    return isPresent
ispresent=isThereElement(list3,12)
print("Is 12 present in list3",ispresent)
#5. Write a function to remove a specific element from an array
list4=[12,34,56,78,90]
print(list4)
# Removing specific element from list4 
list4.remove(56)
print(list4) 
#6. Write a function to copy an array to another array
list5=list4.copy()
print("Copied array",list5)
#7. Write a function to insert an element at a specific position in the array
list5.insert(0,"Inserted Element")
print("Element is inserted at index at 0")
print("The array is ",list5)
#8. Write a function to find the minimum and maximum value of an array
list6=[11,22,182,57,79,105]
max=0
print(list6)
arr1len=len(list6)
for i in range(arr1len):
    if max<list6[i]:
        max=list6[i]
print("Max value of array",max)
#9. Write a function to reverse an array of integer values
list6.reverse()
print("The reversed array is ",list6)
#10. Write a function to find the duplicate values of an array
list7=[101,65,65,23,45,89,89]
comp=[]
arr1_length=len(list7)
for i in range(arr1_length):
    for j in range(i+1,arr1_length):
        if(list7[i]==list7[j]):
            comp.append(list7[i])
print("The duplicates items are",comp)        
#11. Write a program to find the common values between two arrays   
commArr1=[11,12,34,45] 
commArr2=[34,45,99,10,12]
commonEl=[]
for i in range(len(commArr1)):
    for j in range(len(commArr2)):
        if commArr1[i]==commArr2[j]:
            commonEl.append(commArr1[i])   
print("The duplicate items are ",commonEl)
#12. Write a method to remove duplicate elements from an array
#18. Write a program to remove the duplicate elements and return the new array
arr2=[12,34,56,90,12,34,78]
finalarr2=[]
print(arr2)
for i in arr2:
    if i not in finalarr2:
        finalarr2.append(i)
print(finalarr2)
#13. Write a method to find the second largest number in an array
max=0
min=0
for i in range(len(finalarr2)):
    if max<finalarr2[i]:
        min=max
        max=finalarr2[i]
    if finalarr2[i]>min and finalarr2[i]<max:
        min=finalarr2[i]
    
print("Second largest element in array",min)
#14. Write a method to find number of even number and odd numbers in an array
EvenOddarr=[12,34,55,56,79,91]
odd=""
even=""
print(EvenOddarr)
for i in EvenOddarr:
    if(i%2==0):
        even=even+str(i)+" "
    else:
        odd=odd+str(i)+" "
print("The odd numbers are ",odd)
print("The even numbers are",even)
#15. Write a function to get the difference of largest and smallest value
largest=0
smallest=EvenOddarr[1]
for i in EvenOddarr:
    if largest<i:
        largest=i
    if i<smallest:
        smallest=i
print(largest-smallest)
#16. Write a method to verify if the array contains two specified elements(12,23)
arr3=[12,10,34,32,23,56,78,99,102]

for i in arr3:
    if i==12:
        print("Yes the element 12 exists")
    if i==23:
        print("Yes the element 23 exists")