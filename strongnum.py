#program to check if a number is strong or not
def fact(a):
    fac = 1
    for i in range(a+1):
        fac = fac * i
    return fac

n = int(input("enter a number"))
arr = []
s = 0
while(n > 0):
    reminder = n % 10
    arr.append(reminder)
    n = n // 10
for i in range(len(arr)):
    f = fact(arr[i])
    s = s + f
    
if (s == n):
    print("the number is a strong number")
else:
    print("the number is not a strong number")
