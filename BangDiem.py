from decimal import ROUND_HALF_UP, Decimal
from math import ceil


class student:
    def __init__(self, msv, name, d):
        self.msv = msv
        self.name = name 
        self.d = d.quantize(Decimal('0.1'), ROUND_HALF_UP)
def cmp(a):
    return -a.d or a.msv
def convert(s):
    return "HS" + '{:02d}'.format(s)
def rate(x):
    if x >= 9 :
        return "XUAT SAC"
    elif x >= 8:
        return "GIOI"
    elif x >= 7:
        return "KHA"
    elif x >= 5:
        return "TB"
    return "YEU"
a = []    
for i in range(int(input())):
    name = input()
    ls = list(map(Decimal, input().split()))
    d = 2 * ls[0] + 2 * ls[1]
    for t in range(2, 10):
        d += ls[t]
    d /= 12
    o = student(i + 1, name, d)
    a.append(o)
a.sort(key = cmp)
for x in a:
    print(convert(x.msv), x.name, x.d, rate(x.d))
    
