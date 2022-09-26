if x > 0: 
        s += min(x, 50) * 100 * 1.02
        x -= min(x, 50)def cal(x):
    s = 0
    p = 0
    if x > 100 :
        p = 0.05 
    elif x > 50 :
        p = 0.03 
    else :
        p = 0.02
    s += min(x, 50) * 100
    x -= min(x, 50)
    s += min(x, 50) * 150 
    x -= min(x, 50)
    s += x * 200
    s = s + s * p
    return s
class obs:
    id = 1
    def __init__(self, name, s):
        self.ms = 'KH' + '{:02d}'.format(obs.id)
        self.name = name 
        self.s = cal(s)
        obs.id += 1
def cmp(a):
    return -a.s        
a = []
for i in range(int(input())):
    name = input() 
    start = int(input())
    end = int(input())
    o = obs(name, end - start)
    a.append(o)
a.sort(key = cmp)
for x in a :
    print(x.ms, x.name, round(x.s))
