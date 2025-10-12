#Use nested loops to print a multiplication table (1 to 10)
#
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} x {j} = {i*j} ")
#     print("")



# Print numbers from 1 to 50, but:
#
# If divisible by 3 → print "Fizz"
#
# If divisible by 5 → print "Buzz"
#
# If divisible by both → print "FizzBuzz"
# for i in range(1,51):
#     if i % 3 == 0:
#         print(i," = Fizz")
#         if i % 5 == 0:
#             print(i," = Buzz")
#             if i % 3 == 0 and i % 5 == 0:
#                 print(i," = Fizzbuzz")
#
# Print a pattern of numbers in reverse order:
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# num = 5
# for i in range(num,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()


#Write a program that keeps asking for input until the user types “exit”.

string2 = input("Enter a input = ")

while True:
    if string2 == 'exit':
        print("Congrats ! you esacape the loop")
        break
    else:
        print("Please enter Exit to esacape loop ")
        string2 = input("Enter a input = ")