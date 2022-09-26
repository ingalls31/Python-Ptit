class matrix:
    def __init__(self, n, m):
        self.n = n 
        self.m = m 
        self.a = [[0] * m] * n 
        self.b = []
    def input(self):
        for i in range(self.n):
            arr = list(map(int, input().split()))
            self.a[i] = arr
    def convert(self):
        for j in range(self.m):
            arr = []
            for i in range(self.n):
                arr.append(self.a[i][j])
            self.b.append(arr)
    def answer(self):
        for i in range(self.n):
            for j in range(self.n):
                s = 0
                for k in range(self.m):
                    s += self.a[i][k] * self.b[k][j]
                print(s, end = ' ')
            print()
                
test = int(input())
for q in range(test):
    n,  m = list(map(int,input().split()))
    a = matrix(n, m)
    a.input()
    a.convert()
    a.answer()
    # print(a.b)
    
