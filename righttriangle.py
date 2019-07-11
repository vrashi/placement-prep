row = int(input("Enter the number of rows"))
a = 5
for i in range(1, row+1, 1):
    for j in range(1, (row+1) - i, 1):
        print(" ", end = " ")
    for j in range (1, i+1, 1):
        print(a, end = " ")
    a = a + 1
    print()