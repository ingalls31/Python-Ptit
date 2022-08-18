alpha = "0123456789ABCDEFGH"
for t in range(int(input())):
    k = int(input())
    s = input()
    a = 0
    s = s[::-1];
    for i in range(len(s)):
        if s[i] == '1':
            a += 2**i
    ans = ''
    # print(a)
    while a > 0:
        ans += alpha[a % k]
        a //= k
    if a > 0 :ans += str(a)
    ans = ans[::-1]
    print(ans)
    
