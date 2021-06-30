from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))   

s, ex, ey = map(int, input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

data.sort()
queue = deque(data)

while queue:
    v, t, x, y = queue.popleft()

    if t == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append((graph[nx][ny], t+1, nx, ny))

print(graph[ex-1][ey-1])