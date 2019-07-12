#to check if the input character is an alpjabet or not
ch = input("enter a character")
#METHOD 1
#if ch.isalpha() == True:
 #   print("the character is an alphabet")
#else:
 #   print("the character is not an alphabet")
 #METHOD 2
if ch >= "a" and ch <= "z" or ch >= "A" and ch <= "Z":
    print("the character is an alphabet")
else:
    print("the character is not an alphabet")