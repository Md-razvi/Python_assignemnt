#1. Different ways creating a string
#Using double quotes
str1="Word1"
print("Using double quotes ",str1)
str2='Word2'
print("Using sing quotes",str2)
str3="""This
is double string"""
print(str3)
#2. Concatenating two strings using + operator
str4="String 1 "
str5="String 2"
concatenatedString=str4+str5
print(concatenatedString)
#3. Finding the length of the string
str6="0123456789"
lengthOfStr6=len(str6)
print("Length of word str6",lengthOfStr6)
#4. Extract a string using Substring
str7="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
extractedstr=str7[:3]
print("This is a extracted string",extractedstr)
#5. Searching in strings using index()
str8="This a String1"
index=str8.index("Str")
print("This is a words",index)
#6. Matching a String Against a Regular Expression With matches()
import re
matchWord="This is string scan"
matchWord1="This is string scan"
isTrue=re.match(matchWord,matchWord1)
print(isTrue)
print()
#7. Comparing strings using ==
print(matchWord==matchWord1)
#8. startsWith(), endsWith() and compareTo()
str9="Hello World"
starts=str9.startswith("Hel")
ends=str9.endswith("old")
print("This is",starts,ends)
#compareTo () is used ==
#9. Trimming strings with strip()
spaces_Str="   String with spaces       "
print(spaces_Str)
withOut_Spaces=spaces_Str.strip()
print(withOut_Spaces)
#10 Replacing characters in strings with replace()
str10=str9.replace("World","Duniya")
print(str10)
#11. Splitting strings with split()
print('https:\www.google.com\\Hello World')
str11='https:\\www.google.com\\Hello World'
str12=re.split(r'[\\]',str11)
print(str12)
#12. Converting integer objects to Strings
intObject=12
print("The given number",intObject,"is",type(intObject))
str13=str(intObject)
print('The given number',str13,'is',type(str13),"after convertion")
#13. Converting to uppercase and lowercase
str14='This is a python programming'
str15=str14.lower()
print(str15)
str16=str14.upper()
print(str16)