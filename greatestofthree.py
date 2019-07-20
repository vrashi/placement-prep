#program to find the greatest of the three numbers
print("enter three numbers")
a = int(input())
b = int(input())
c = int(input())
if (a >= b) and (a >= c):
    print(a, " is the greatest number")
elif (b >= a) and (b >= c):
    print(b, " is the greatesr number")
elif (c >= a) and (c >= b):
    print(c, " is the greatest number")
elif (a == b) and (b == c):
    print("all three numbers are equal")