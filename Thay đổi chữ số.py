def solution():
    p,q = input().split()
    a = input().strip()
    if a.count(' '):
        a, b = a.split()
    else :
        b = input()
    p = min(p, q)
    q = max(p, q)
    print(int(a.replace(q,p)) + int(b.replace(q,p)), end = ' ')
    print(int(a.replace(p,q)) + int(b.replace(p,q)))
for t in range(int(input())):
    solution()
