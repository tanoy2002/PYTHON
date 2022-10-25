electronics=["pc","laptop","tablet","phablet","earphones","Headphones","Mic","speakers"]
print(electronics)
print(electronics[3])
numbers=[1,4,5,6,7,8,9,10,11,12,2,15,19,13,3]
print(numbers[5])#print number on 5th position starting from 0
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
print(numbers[:15])
a=len(numbers)
print(a)
#print(numbers[:b])
print(numbers[::-3])#negative numbers only work when the first two indexes are not present or kept blank
print(max(numbers))
print(min(numbers))
#some list methods
numbers.append(67)
numbers.append(478)
numbers.append(789)
numbers.insert(0,6789)
numbers.insert(3,890)
numbers.remove(15)#put the element to be removed
numbers.pop()#put the index of the element to be removed
print(numbers)
tp=(1,7,9)
print(tp)
a=47
b=45
#First way to swap two numbers
temp=a
a=b
b=temp
print(a,b)
#second and more efficient way of swapping numbers
a,b=b,a
print(a,b)
print(type(numbers))
print(type(electronics))
