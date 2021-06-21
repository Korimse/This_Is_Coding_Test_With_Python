from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    queue.append((nx, ny))

count = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bfs(i, j)
            count += 1
print(count)