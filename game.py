d=l=0
s=input("Enter the letters with digit")
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters",l)
print("Digital",d)