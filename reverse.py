n = int(input("enter a number"))
r = []
while n>0:
    m = n%10
    r.append(m)
    n = n // 10
print(r)
for i in r:
    print(i,end="")