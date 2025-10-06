# Q. Find out the maximum no of given  3 numbers
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 >= num2 and num1 >= num3:
    print("Number1 is greater than or equal to other numbers.")
elif num2 >= num1 and num2 >= num3:
    print("Number2 is greater than or equal to other numbers.")
else:
    print("Number3 is greater than or equal to other numbers.")
