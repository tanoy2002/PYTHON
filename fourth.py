#checking how string slicing works
str1="This is an example"
str2="hfhfhdsfkhjf"
print(str1[0:4])
print(len(str1))
print(str1[0:18])
print(str1[0:])
print(str1[:18])
print(str1[::1])
print(str1[::-1])
print(str1[::2])
print(str1[::-2])
print(str1[::-5])
#some new functions
print(str1.isalnum())
print(str1.isalpha())
print(str1.endswith("example"))
print(str1.count("i"))
print(str2.capitalize())
print(str2.find("k"))
print(str1.lower())#lower case
print(str2.upper())#upper case
print(str1.replace("This","These"))#replace with new word
#useful way of printing a string with a huge value
x=len(str1)
print(str1[0:x])
#or
print(str1[:x])
