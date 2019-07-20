#program to find the power of a number
base = int(input("enter the base number"))
exp = int(input("enter the exponential power"))
res = 1
for i in range(1, exp + 1):
    res = res * base
print(res)

