#program to find the greatest of two numbers
print("enter two numbers")
a = int(input())
b = int(input())
if a > b:
    print(a, " is greater than ", b)
elif b > a:
    print(b, " is greater than ", a)
else:
    print("the two numbers are equal")