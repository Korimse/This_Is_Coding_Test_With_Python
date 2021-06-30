from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [999999] * (n+1)
queue = deque()
queue.append(x)
visited[x] = 0
while queue:
    v = queue.popleft()
    for i in graph[v]:
        tmp = visited[v] + 1
        if tmp < visited[i]:
            visited[i] = tmp
            queue.append(i)

answer = []
for v in range(len(visited)):
    if visited[v] == k:
        answer.append(v)

if len(answer) == 0:
    print(-1)
else:
    for v in answer:
        print(v)