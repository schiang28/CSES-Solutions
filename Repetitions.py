x=input()

c,m=1,1
for i in range(len(x)-1):
    if x[i] == x[i+1]:
        c+=1
        if c>m:
            m=c
    else:
        c=1

print(m)