#program to find sum of all the digits of an integer
n = int(input("enter a number"))
s = 0
while n>0:
    remainder = n % 10
    s = s + remainder
    n = n//10
print(s)