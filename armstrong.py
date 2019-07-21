#program to check if a number is armstromg or not

#n is the number user enters to check
n = int(input("enter a number"))
#s is the sum of cube of all the digits of the number n
#armsrtong number = s should be the same as n
s = 0
while (n > 0):
    remainder = n % 10
    s = s + (remainder * remainder * remainder)
    n = n // 10
print(s)
print(type(s))
if (n == s):
    print("the given number is an armstrong number")
elif (n != s):
    print("the given number is not an armstrong number")


