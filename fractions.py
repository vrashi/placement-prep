#program to add two fractions

def lcm(d1, d2):
    high = 0
    if d1 >= d2:
        high = d1 
    else:
        high = d2
    for i in range(high, (d1 * d2) + 1):
        if (i % d1 == 0) and (i % d2 == 0):
            return i
        else:
            return d1 * d2

n1 = int(input("enter numerator of the first number"))
d1 = int(input("enter denominator of the first number"))
n2 = int(input("enter numerator of the second number"))
d2 = int(input("enter denominator of the second number"))

D = lcm(d1, d2)
N1 = (D / d1) * n1
N2 = (D / d2) * n2
N = N1 + N2
print("the sum is", int(N), "/", D)

