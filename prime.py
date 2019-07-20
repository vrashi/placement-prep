#program to check if a number is prime or not
n = int(input("enter a number"))
state = True
for i in range(2, n):
    if n % i == 0:
        state = False
if state == True:
    print("the number is prime")
elif state == False:
    print("the number is not prime")
