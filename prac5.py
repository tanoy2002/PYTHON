# #Print patterns similar to those as shown below for any no of inputs :
# 1. *
#    * *
#    * * *
#    * * * *
#    * * *
#    * *
#    *
#
# 2.  1
#     1 2
#     1 2 3
#     1 2 3 4
#     1 2 3
#     1 2
#     1

# for 1.:
#   method1-
# x=int(input())
# for i in range(1,x+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print()
# for i in range(x,0,-1):
#     for j in range(i-1,0,-1):
#         print("* ",end="")
#     print()

#or Method 2-
x=5
for i in range(1,x+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()
for i in range(1,x+1):
    for j in range(1,x):
        print("* ",end="")
    x=x-1
    print()

# n = 10
# for i in range(1, 2*n):
#   if i <= n:
#     print(i*"* ")
#   else:
#     print((2*n - i)*"* ")
