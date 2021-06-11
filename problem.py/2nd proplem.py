a=input("Enter any string or integer: ")
b=len(a)
flag=False
for i in range(b):
    if a[i]!=a[-(i+1)]:
        flag=True
        break
if flag:
    print(a, "is a not a palindrome")
else:
    print(a, "is a palindrome")
