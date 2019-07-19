#program to find lcm of two numbers by modulus method
print("enter two numbers")
a = int(input())
b = int(input())
high = 0
if (a > b):
    high = a
else:
    high = b
for i in range(high, (a*b)+1):
    if (i % a == 0) and (i % b == 0):
        print(i)
    else:
        print(a*b)
    break