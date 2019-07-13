#program to find factorial
n = int(input("enter the number to fing factorial"))
fac = 1
for i in range(1, n + 1, 1):
    fac = fac*i
print(fac)