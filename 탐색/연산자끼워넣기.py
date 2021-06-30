n = int(input())

arr = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

maxv = -9999999
minv = 999999

def dfs(i, now):
    global add, sub, mul, div, maxv, minv
    if i == n:
        minv = min(minv, now)
        maxv = max(maxv, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + arr[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - arr[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * arr[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(now/arr[i]))
            div += 1
dfs(1, arr[0])

print(maxv)
print(minv)