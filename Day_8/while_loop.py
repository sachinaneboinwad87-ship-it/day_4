#Print even numbers between 1 to 50 using a while loop.
number = 1
while number <=  50:
    if number % 2 == 0:
        print(number)
    number += 1

#Calculate the sum of digits of a number using a while loop.

# Takes the input of N given by the user
N = int(input("Enter the value of N: "))

# Initialize the variables 'count' and 'total'
count = N
total = 0

while count:
    total += count
    count -= 1

#