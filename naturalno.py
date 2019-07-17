#sum of n natural numbers
n = int(input("enter a natural number"))
s = 0
for i in range(1, n + 1, 1):
    s = s + i  
print(s)