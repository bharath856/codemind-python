s=input()
r=s.lower()
c=0
for i in r:
    if r.count(i)==1:
        if i!=' ':
            c+=1
print(c)