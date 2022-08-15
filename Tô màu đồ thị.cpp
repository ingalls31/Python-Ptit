def dfs(u, pre):
    for i in range(1,21):
        dp[u][i] = i
    for x in g[u]:
        if x == pre:
            continue
        dfs(x, u)
        for i in range(1,21):
            value = int(1e18)
            for j in range(1,21):
                if i != j:
                    value = min(value, dp[x][j])
            dp[u][i] += value
    pass

for t in range(int(input())):
    n = int(input())
    dp = [[0 for i in range(25)] for j in range(n + 5)]
    g = [[] for i in range(n + 5)]
    a = [int(x) for x in input().split()]
    for i in range(n):
        g[a[i]].append(i + 1)
    dfs(1, 0)
    print(min(dp[1][1:21])) 
