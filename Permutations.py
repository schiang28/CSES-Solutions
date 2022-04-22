x=int(input())

ls = []
for i in range(2,x+1,2):
    ls.append(str(i))
for i in range(1,x+1,2):
    ls.append(str(i))

if len(ls) >= 4 or len(ls)==1:
    print(' '.join(ls))
else:
    print("NO SOLUTION")