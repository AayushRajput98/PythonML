s=input("Enter the STRING: ")
#row=int(input("Enter the number of rows: "))
for i in range(0, len(s)):
    if i % 4 == 0:
        print(s[i], end="")
    else:
        print(" ", end="")
print()
for i in range(0, len(s)):
    if not i % 2 == 0 and not i == 0:
        print(s[i], end="")
    else:
        print(" ", end="")
print()
for i in range(0, len(s)):
    if i % 2 == 0 and not i % 4 == 0 and not i == 0:
        print(s[i], end="")
    else:
        print(" ", end="")
