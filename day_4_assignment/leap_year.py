# Q. Write a code for given year is leap year or not .
year = int(input("Enter a year : "))

if year % 4 == 0:
    print(f"{year}  is leap year  ")
else:
    print("Given year is not leap year ")