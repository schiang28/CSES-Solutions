from itertools import combinations

def method1():
    def hamming(m,n):
        count = 0
        for i in range(len(m)):
            if m[i] != n[i]:
                count+=1
        
        return count

    a,k = list(map(int, input().split()))

    minh = 999
    ls = []

    for _ in range(a):
        ls.append(input())

    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            h = hamming(ls[i], ls[j])
            if h < minh:
                minh=h

    print(minh)

def xormethod():
    n,k = map(int, input().split())
    ans = 999
    num = [input() for _ in range(n)]

    for a in range(len(num)):
        for b in range(a+1, len(num)):
            r = int(num[a], 2)^int(num[b], 2)
            ans = min(bin(r)[2:].count('1'), ans)

    print(ans)

def xorcomb():
    n,k = map(int, input().split())
    num = [input() for _ in range(n)]
    ans = 999

    for a,b in combinations(num, 2):
        result = int(a, 2)^int(b, 2)
        ans = min(bin(result)[2:].count("1"), ans)

    print(ans)