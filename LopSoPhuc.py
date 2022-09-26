for test in range(int(input())):
    a, b, c, d = list(map(int, input().split()))
    s1 = complex(a, b)
    s2 = complex(c, d)
    ans1 = (s1 + s2) * s1
    ans2 = (s1 + s2) ** 2
    print("%d + %di, %d + %di" % (ans1.real, ans1.imag, ans2.real, ans2.imag))
    
