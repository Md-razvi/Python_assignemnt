# Create a Dictionary with at least 5 key value pairs of the Student ID and Name
Student_Details={
    "101":"Rajesh",
    "102":"Mahia",
    "103":"Ram",
    "104":"Sham",
    "105":"Azhar"
}
print(Student_Details)
# Adding the values in dictionary
Student_Details["106"]="Saba"
print(Student_Details)
# Updating the values in dictionary
Student_Details.update({"107":"Saba"})
print(Student_Details)
# Accessing the value in dictionary
for i in range(1,6):
    value=100+i
    value1=str(value)
    print(Student_Details[value1],end=" ")
print(" ")
# Create a nested loop dictionary
MyDiction={
    "data1":{"Student_Id":11203,"Student_name":"Raza"},
    "data2":{"Student_Id":11204,"Student_name":"Sham"},
    "data3":{"Student_Id":11205,"Student_name":"GhanSham"},
    "data4":{"Student_Id":11206,"Student_name":"Balram"},
    "data5":{"Student_Id":11207,"Student_name":"Ram"},
    "data6":{"Student_Id":11208,"Student_name":"Bahdur"}
}
print(MyDiction)
# Access the values of nested loop dictionary
for i in range(1,len(MyDiction)+1):
    value="data"+str(i)
    print(MyDiction[value]["Student_Id"],MyDiction[value]["Student_name"])
# Or
for x in MyDiction.values():
    print(x["Student_Id"]," ",x["Student_name"],end="\t\t")
# Print the keys present in a particular dictionary
print(" ")
for x in MyDiction.keys():
    print(x,end="\t\t")
# Delete a value from a dictionary
MyDiction.pop("data6")
print(MyDiction)    
    