# lst=["a","b","c","d","e","f","g"]
# print(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6])#tedious way of printing the elements in a list
# for item in lst:
#   print(item)
# lst1=[["a",1],["b",2],["c",3],["d",4],["e",5],["f",6],["g",7]]
# dict1=dict(lst1)
# print(dict1)
# for item,quant in lst1:
#   print(item,quant)#for printing multiple elements
# for item,quant in lst1:
#   print(item,"has the quantity",quant)
# for item,quant in dict1.items():#dictionary cannot be used directly like in list or tuples-use of the items() function is necessary for extraction of items
#   print(item,"has the quantity",quant)
# #in dictionary it is necessary to extract using items() if keys and the corresponding values are required to be printed otherwise the same procedure can be followed as is for list and tuples
# #example illustrated below
# for item in dict1:
#   print(item)#works normally like lists or tuples



###Practice exercise
list1=[1,7,9,4,6,"t","a",14,"g","h","l",10,8,43,"b",2,"c"]
for x in list1:
  if type(x)==int and x>6:
    print(x)
#or another approach using .isnumeric() function
list1=[1,7,9,4,6,"t","a",14,"g","h","l",10,8,43,"b",2,"c"]
for x in list1:
  if str(x).isnumeric() and x>6:#typecasting is necessary in case you want to use isnumeric() function as it takes input as strings and the integer values cannot be recognonized, hence giving an error
    print(x)
