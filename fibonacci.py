#program to get Fibonacci serise upto n
n = int(input("enter a number"))
arr = []
arr.append(1)
arr.append(1)
for i in range(2, n, 1):
    arr.append(arr[i-1] + arr[i-2])
print(arr)