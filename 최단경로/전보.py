import heapq

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
maxv = 0
for d in distance:
    if d != INF:
        count += 1
        maxv = max(maxv, d)
print(count -1, maxv)