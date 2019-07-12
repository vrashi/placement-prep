# to print the usside-down triangle of digits
row = int(input("Enter number of rows"))
a = row
for i in range(row+1, 0, -1):
    for j in range(i+1, 2, -1):
        print(a, end = " ")
        a = a - 1
    print()
    a = row

