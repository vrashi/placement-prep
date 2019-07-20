#program to find HCF of GCD of two numbers
print("enter two numbers")
a = int(input())
b = int(input())
low = 0
if a <= b:
    low = a
else:
    low = b
print(low)
for i in range (1, low + 1, 1):
    if ((a % i == 0) and (b % i == 0)):
        hcf = i
print("the hcf is ", hcf)