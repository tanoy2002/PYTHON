# checking how dictionary works
a={"Rajiv":"Shukla","Naman":"Ahuja","Taimur":"Khan","Yashashvi":"Sharma","Maya":"Collins","Aditi":"Shukla","Shubham":{"b":"Sandwhich","l":"Poori","d":"Sabzi"}}
print(a["Yashashvi"])#searches the name and finds out what it corresponds to
print(a["Maya"])
print(a["Aditi"])
print(a["Taimur"])
print(a["Shubham"]["l"])#Searches the name and finds out what it corresponds to and searches for the specific correspondence 'l' as mentioned
#adding new entries to the dictionary
a["Gorba"]="Kaka"#adding a new entry to the dictionary
a["Hagemaru"]="Moin"
a[67]="Example"
print(a)
del a[67]
print(a)
b=a.copy()#a copy of 'a' has been stored in 'b'
del b["Rajiv"]#deleted an element from the dictionary 'b'
print(a)#printing 'a' will print the actual set of elements from 'a' as 'a' hasnt been modified
print(b)#printing 'b' will print the modified 'a' table which has been stored in the dictionary 'b'
print(a.get("Taimur"))#another way of fetching an element using the 'get' function
a.update({"Aliya":"Bhatt"})#another way of adding a new entry to the dictionary using the update function
print(a)
print(a.keys())#key function prints the set of key entries that are used to fetch the corresponding entries
print(a.items())#items function prints each pair of key value entries along with its corresponding values
help()
