#matrices
a = [[0 for x in range(2)] for y in range(2)]
#print("enter the coefficient of x and y of first equation and then 2nd equation")
tmp = [1, 1, 2, 4]
#temp = input("enter the coefficient of x and y of first equation and then 2nd equation")
#tmp = temp.split()

for i in range(2):
    for j in range(2):
        a[0][i] = tmp[j]
a[1][0] = 2
a[1][1] = 4
print(a)

a_inverse = [[0 for x in range(2)] for y in range(2)]
D1 = a[0][0]*a[1][1]
D2 = a[0][1]*a[1][0]
D = 1/(D1 - D2)
a_inverse[0][0] = D*a[1][1]
a_inverse[0][1] = -D*a[0][1]
a_inverse[1][0] = -D*a[1][0]
a_inverse[1][1] = D*a[0][0]
print (a_inverse)
b = [4, 10]
#b = input("enter RHS")
x = [0, 0]
p = (a_inverse[0][0]*b[0])
q = (a_inverse[0][1]*b[1])
x[0] = p + q
r = (a_inverse[1][0]*b[0])
s = (a_inverse[1][1]*b[1])
x[1] = r + s
print (x)
