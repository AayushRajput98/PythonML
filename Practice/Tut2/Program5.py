d={}
print(ord('Z'))
for i in range(65,77):
    d.setdefault(chr(i),chr((i+12)))
    d.setdefault(chr(i+32),chr((i+44)))
for i in range(77,91):
    d.setdefault(chr(i), chr((i + 12)%90+65))
    d.setdefault(chr(i + 32), chr((i + 44)%122+97))
print(d)
d[" "]=" "
s=input("Enter the string to be converted in ROT-13: ")
s1=""
for i in s:
    s1=s1+d[i]
print(s1)
