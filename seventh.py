#learning how sets work
s=set()
# print(type(s))
# setex=set([1,2,3,4])
# print(type(setex))
# #eitherwise
# a=[1,2,3,4]
# setex2=set(a)
# print(type(setex2))
s.add(1)#adding new value to s
s.add(1)#only unique values are retained in the set
s.add(2)
s1=s.union({1,2,3})#prints the union of the two sets
s2=s.intersection({1,2,3})#prints the intersection of the two sets
print(s,s1,s2)
print(s1|s)#another way to print union
print(min(s))
print(max(s))
print(max(s1))
s3={4,5,6}#this format is for a set
print(type(s3))
print(s.isdisjoint(s3))#for checking if two sets are disjoint
s.remove(2)
print(s)
s.add(2)
print(s)
