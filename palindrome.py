#program to check if a sequence is a palindrome or not

s1 = input("enter a sequence")
s2 = []
for i in range(len(s1)-1, -1, -1):
    s2.append(s1[i])
print(s2)
state = True
for i in range(len(s2)):
    if s1[i] != s2[i]:
        state = False
    #else:
     #   print("given sequence is not a palindrome")

if state == True:
    print("given sequence is a palindrome")
else:
    print("given sequence is not a palindrome")