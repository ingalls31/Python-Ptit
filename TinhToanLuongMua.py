tt = 1
ls = {}

def cal(start, end): 
    a =list(map(int, start.replace(":", " ").split())) 
    b = list(map(int, end.replace(":", " ").split()))
    h = b[0] - a[0]
    p = b[1] - a[1]
    h += p / 60
    return h
for i in range(int(input())):
    name = input()
    start = input()
    end = input()
    s = int(input())
    if name not in ls.keys():
        ls[name] = [tt, cal(start, end), s]
        tt += 1
    else:
        o = ls.get(name)
        ls[name] = [o[0], o[1] + cal(start, end), o[2] + s]

for key, value in ls.items():
    print("T0", end = '')
    print(value[0], key, "{:.2f}".format(value[2] / value[1]))
    
