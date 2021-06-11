a=input("Enter any string: ")
b=int(input("Enter a key value: "))
s=""
for i in a:
    s+=chr(ord(i)+b)
print(s, " is the Encrypted form with key",b)
print(a, " is the Decrypted form with key",b)
