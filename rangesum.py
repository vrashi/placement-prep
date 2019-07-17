#sum of n natural numbers
print("enter a range")
a = int(input())
b = int(input())
s = 0
for i in range(a, b + 1, 1):
    s = s + i
print("the sum of numbers in the given range is "+str(s))