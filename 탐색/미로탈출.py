from collections import deque

n, m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input())))

visited = [[0]*m for i in range(n)]
visited[0][0] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

print(visited[n-1][m-1])