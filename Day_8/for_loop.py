# Print a multiplication table of a given number.
# num =int(input(" Enter the number : "))
# for i in range(1,11):
#     i *= num
#     print(i)
from math import factorial

#Find the largest number in a list without using max().
# numbers= [10,20, 13,56, 47, 89,36,66]
# largest=  numbers[0]
# for num in numbers:
#     if num  > largest:
#         largest =  num
# print(largest)
#
# #Find the factorial of a given number.
# num =  int(input("Enter a number : "))
# result = 1
# for i in range(1,num+1):
#     result = result * i
#
# print("Factorial of", num, "is", result)

#Print all numbers from 1–100 divisible by both 3 and 5.
for i in range(1,101):
    if i % 3== 0 and i % 5 == 0:

        print(i," : This number is divided by 3 and 5")


