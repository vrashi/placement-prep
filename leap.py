#program to check if a year is leap or not
year = int(input("enter a year"))
if year % 4 == 0:
    print(year, " is a leap year")
else:
    print(year, "is not a leap year")