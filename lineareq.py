#matrices
a = [[0 for x in range(2)] for y in range(2)]
#print("enter the coefficient of x and y of first equation and then 2nd equation")
temp = [4]
temp = input("enter the coefficient of x and y of first equation and then 2nd equation")
tmp = temp.split()

for i in range(2):
    for j in range(2):
        a[0][i] = tmp[j]

for i in range(2):
    for j in range(2, 4):
        a[1][i] = tmp[j]
#print(a)

a_inverse = [[0 for x in range(2)] for y in range(2)]
a_inverse[0][0] = a[1][1]
a_inverse[0][1] = -a[0][1]
a_inverse[1][0] = -a[1][0]
a_inverse[1][1] = a[0][0]
#print (a_inverse)
b = [2]
b = input("enter RHS")
x = [2]
x = a_inverse*b
print (x)
