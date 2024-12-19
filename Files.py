# Write a program to read text file
f=open('text.txt',"r")
print(f.read())
# Write a program to write text to .txt file using InputStream
newFile=open('WrittenText.txt',"w")
newFile.write("This is file written by python programming language  please \ncarefully update it, thank you")
newFile.close()
f1 = open("text.txt", "r")
print(f1.read(20))
