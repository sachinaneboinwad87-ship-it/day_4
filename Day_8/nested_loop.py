
# q.1 Print numbers in this pattern:
#
# 1 2 3
# 4 5 6
# 7 8 9

# num = 1
# for i in range(3):
#     for j in range(3):
#         print(num,end=" ")
#         num += 1
#     print()
#

# Q.2 Print a right triangle of stars:

# *
# * *
# * * *
# * * * *
# n= 4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

#
# q.3 Print an inverted triangle:
#
# * * * *
# * * *
# * *
# *
# n = 4
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print("*",end=" ")
#     print()

#q.4 Print a square of numbers (rows = columns = 5):
#
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# num = 5
# for i in range(5):
#     for j in range(1,num+1):
#         print(j,end=" ")
#     print( )

# q. 5 Print this pattern:
#
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
#
# num = 5
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#
# q.6 Create a pattern where each row prints the row number repeated:
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
#
# num = 4
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#
# rint this number pattern:
#
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
# num = 5
# for i in range(num):
#     for j in range(num,i,-1):
#         print(j,end = " ")
#     print()